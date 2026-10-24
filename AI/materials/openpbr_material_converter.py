"""
KeyShot OpenPBR Material Converter v0.5.0
Converts supported KeyShot materials to OpenPBR (lux_openpbr)
using dictionary-based parameter lookups.

Preserves texture and utility node connections (edges) by:
 1. Cataloging all input edges on the source shader
 2. Mapping old parameter names to OpenPBR parameter names
 3. Reconnecting source nodes to the new OpenPBR node

v0.5.0 additions:
 - Mode dialog: batch (all materials) or individual selection
 - Roughness conversion: KeyShot * 4.0 clamped to 1.0
 - Emissive intensity conversion: KeyShot * 667.0
 - Emissive emission_weight = 1.0 fixed value
 - Thin film thickness nm -> 0.0-1.0, IOR offset -0.1
 - Transmissive materials: IOR, depth, dispersion mappings
 - Glass Window removed from COLOR_MAP (no base_color)
 - Orphan node cleanup pass after conversion

Graph structure: __root <- 'surface' <- shader node <- edges <- texture/utility nodes
"""

import lux

OPENPBR_TYPE = 'lux_openpbr'
VERSION = "0.5.0"

ROUGHNESS_PARAMS = {
   'specular_roughness',
   'coat_roughness',
   'base_diffuse_roughness',
   'fuzz_roughness',
}

COLOR_MAP = {
   lux.SHADER_TYPE_DIFFUSE:              ('diffuse',      True),
   lux.SHADER_TYPE_ADVANCED:             ('diffuse',      True),
   lux.SHADER_TYPE_PLASTIC:              ('diffuse',      True),
   lux.SHADER_TYPE_PLASTIC_TRANSPARENT:  ('diffuse',      True),
   lux.SHADER_TYPE_PLASTIC_CLOUDY:       ('transmission', False),
   lux.SHADER_TYPE_METAL:                ('color',        True),
   lux.SHADER_TYPE_PAINT:                ('color',        True),
   lux.SHADER_TYPE_METALLIC_PAINT:       ('base',         True),
   lux.SHADER_TYPE_ANISOTROPIC:          ('diffuse',      True),
   lux.SHADER_TYPE_TRANSLUCENT:          ('diffuse',      False),
   lux.SHADER_TYPE_TRANSLUCENT_MEDIUM:   ('diffuse',      True),
   lux.SHADER_TYPE_EMISSIVE:             ('color',        True),
   lux.SHADER_TYPE_THIN_FILM:            ('color_filter', False),
   lux.SHADER_TYPE_DIELECTRIC:           ('transmission', False),
   lux.SHADER_TYPE_GLASS_SOLID:          ('color',        False),
   lux.SHADER_TYPE_VELVET:               ('diffuse',      False),
   lux.SHADER_TYPE_FLAT:                 ('color',        True),
   lux.SHADER_TYPE_GEM:                  ('color',        False),
   lux.SHADER_TYPE_LIQUID:               ('color',        False),
   lux.SHADER_TYPE_GENERIC:              ('base_color',   True),
}

SPECULAR_MAP = {
   lux.SHADER_TYPE_ADVANCED:            'specular',
   lux.SHADER_TYPE_PLASTIC:             'specular',
   lux.SHADER_TYPE_PLASTIC_TRANSPARENT: 'specular',
   lux.SHADER_TYPE_METALLIC_PAINT:      'metal',
   lux.SHADER_TYPE_ANISOTROPIC:         'specular',
   lux.SHADER_TYPE_TRANSLUCENT:         'specular_color',
   lux.SHADER_TYPE_TRANSLUCENT_MEDIUM:  'specular',
}

ROUGHNESS_MAP = {
   lux.SHADER_TYPE_ADVANCED:            'roughness',
   lux.SHADER_TYPE_PLASTIC:             'roughness',
   lux.SHADER_TYPE_PLASTIC_TRANSPARENT: 'roughness',
   lux.SHADER_TYPE_PLASTIC_CLOUDY:      'roughness',
   lux.SHADER_TYPE_METAL:               'roughness',
   lux.SHADER_TYPE_PAINT:               'roughness',
   lux.SHADER_TYPE_METALLIC_PAINT:      'metal_roughness',
   lux.SHADER_TYPE_ANISOTROPIC:         'roughness_x',
   lux.SHADER_TYPE_TRANSLUCENT:         'roughness',
   lux.SHADER_TYPE_TRANSLUCENT_MEDIUM:  'roughness',
   lux.SHADER_TYPE_DIELECTRIC:          'roughness',
   lux.SHADER_TYPE_GLASS_SOLID:         'roughness',
   lux.SHADER_TYPE_GEM:                 'roughness',
   lux.SHADER_TYPE_GENERIC:             'roughness',
}

EXTRA_MAP = {
   lux.SHADER_TYPE_DIFFUSE: {
       'fixed':  {'specular_weight': 0.0},
       'floats': {'base_diffuse_roughness': 'roughness'},
   },
   lux.SHADER_TYPE_PLASTIC_TRANSPARENT: {
       'fixed':  {'transmission_weight': 1.0},
       'colors': {'transmission_color': 'specular_transmission'},
   },
   lux.SHADER_TYPE_METAL: {
       'fixed': {'base_metalness': 1.0},
   },
   lux.SHADER_TYPE_PAINT: {
       'fixed': {'coat_weight': 1.0, 'coat_darkening': 1.0},
   },
   lux.SHADER_TYPE_METALLIC_PAINT: {
       'fixed':  {'base_metalness': 1.0, 'coat_weight': 1.0, 'coat_darkening': 0.0},
       'colors': {'coat_color': 'clearcoat'},
       'floats': {
           'base_diffuse_roughness': 'metal_roughness',
           'coat_roughness':         'roughness',
           'coat_ior':               'ior',
       },
   },
   lux.SHADER_TYPE_ANISOTROPIC: {
       'floats': {'specular_roughness_anisotropy': 'roughness_y'},
   },
   lux.SHADER_TYPE_TRANSLUCENT: {
       'colors': {'subsurface_color': 'transmission'},
       'floats': {'subsurface_weight': 'translucency'},
   },
   lux.SHADER_TYPE_TRANSLUCENT_MEDIUM: {
       'colors': {'subsurface_color': 'transmission'},
       'floats': {'subsurface_weight': 'translucency'},
   },
   lux.SHADER_TYPE_EMISSIVE: {
       'fixed':  {'emission_weight': 1.0},
       'colors': {'emission_color': 'color'},
       'floats': {'emission_luminance': 'intensity'},
   },
   lux.SHADER_TYPE_THIN_FILM: {
       'fixed':  {'thin_film_weight': 1.0, 'transmission_weight': 1.0},
       'floats': {'thin_film_ior': 'ior', 'thin_film_thickness': 'thickness'},
   },
   lux.SHADER_TYPE_DIELECTRIC: {
       'fixed':  {'transmission_weight': 1.0, 'geometry_thin_walled': False},
       'colors': {'transmission_color': 'transmission'},
       'floats': {
           'specular_ior':                  'ior',
           'transmission_depth':            'thickness',
           'transmission_disp_abbe_number': 'abbe_number',
       },
   },
   lux.SHADER_TYPE_GLASS_SOLID: {
       'fixed':  {'transmission_weight': 1.0, 'geometry_thin_walled': False},
       'colors': {'transmission_color': 'color'},
       'floats': {
           'specular_ior':       'ior',
           'transmission_depth': 'transparency',
       },
   },
   lux.SHADER_TYPE_GLASS: {
       'fixed':  {'transmission_weight': 1.0, 'geometry_thin_walled': True},
       'colors': {'transmission_color': 'transmission'},
       'floats': {
           'specular_ior': 'ior',
       },
   },
   lux.SHADER_TYPE_VELVET: {
       'fixed':  {'base_weight': 1.0, 'specular_weight': 0.0, 'fuzz_weight': 1.0},
       'colors': {'fuzz_color': 'sheen'},
       'floats': {
           'base_diffuse_roughness': 'roughness',
           'fuzz_roughness':         'roughness',
       },
   },
   lux.SHADER_TYPE_FLAT: {
       'fixed': {'specular_weight': 0.0},
   },
   lux.SHADER_TYPE_GEM: {
       'fixed':  {'transmission_weight': 1.0},
       'floats': {
           'specular_ior':                  'ior',
           'transmission_depth':            'transparency',
           'transmission_disp_abbe_number': 'abbe_number',
       },
   },
   lux.SHADER_TYPE_LIQUID: {
       'fixed':  {'transmission_weight': 1.0, 'geometry_thin_walled': False},
       'floats': {
           'specular_ior':       'ior',
           'transmission_depth': 'transparency',
       },
   },
   lux.SHADER_TYPE_GENERIC: {
       'floats': {'base_metalness': 'metallic'},
   },
}

COMMON_EDGE_MAP = {
   'bumpmap':      'geometry_normal',
   'opacitymap':   'geometry_opacity',
   'displacement':  'geometry_normal',
}

SUPPORTED_TYPES = set(COLOR_MAP.keys()) | {lux.SHADER_TYPE_GLASS}

def _strip_alpha(value):
   if isinstance(value, (tuple, list)) and len(value) == 4:
       return value[:3]
   return value

def _find_source_shader(material_graph):
   for shader_type in SUPPORTED_TYPES:
       nodes = material_graph.getNodesFromType(shader_type)
       if nodes:
           return nodes[0], shader_type
   return None, None

def _build_param_map(shader_type):
   param_map = {}
   if shader_type in COLOR_MAP:
       old, strip = COLOR_MAP[shader_type]
       param_map[old] = ('base_color', strip)
   if shader_type in SPECULAR_MAP:
       param_map[SPECULAR_MAP[shader_type]] = ('specular_color', False)
   if shader_type in ROUGHNESS_MAP:
       param_map[ROUGHNESS_MAP[shader_type]] = ('specular_roughness', False)
   extras = EXTRA_MAP.get(shader_type, {})
   for openpbr_p, src_p in extras.get('colors', {}).items():
       param_map[src_p] = (openpbr_p, True)
   for openpbr_p, src_p in extras.get('floats', {}).items():
       param_map[src_p] = (openpbr_p, False)
   for old_p, new_p in COMMON_EDGE_MAP.items():
       if old_p not in param_map:
           param_map[old_p] = (new_p, False)
   return param_map

def _set_param(node, param_name, value):
   try:
       param = node.getParameter(param_name)
       if param is None:
           print(f"    [FAIL] OpenPBR has no parameter '{param_name}'")
           return False
       param.setValue(value)
       print(f"    [SET]  '{param_name}' = {value}")
       return True
   except Exception as e:
       print(f"    [FAIL] Set '{param_name}' = {value}: {e}")
       return False

def _convert_roughness_ks_to_openpbr(val):
   return min(val * 4.0, 1.0)

def _convert_intensity_ks_to_openpbr(val):
   return val * 667.0

def _convert_thinfilm_thickness_ks_to_openpbr(nm):
   result = (nm - 380.0) / 400.0
   return max(0.0, min(result, 1.0))

def _convert_thinfilm_ior_ks_to_openpbr(ks_ior):
   return ks_ior - 0.1

def _apply_value_conversions(param_name, value):
   if param_name in ROUGHNESS_PARAMS and isinstance(value, (int, float)):
       converted = _convert_roughness_ks_to_openpbr(value)
       print(f"    [CONV] Roughness '{param_name}': {value} -> {converted}")
       return converted, True
   if param_name == 'emission_luminance' and isinstance(value, (int, float)):
       converted = _convert_intensity_ks_to_openpbr(value)
       print(f"    [CONV] Intensity '{param_name}': {value} -> {converted}")
       return converted, True
   if param_name == 'thin_film_thickness' and isinstance(value, (int, float)):
       converted = _convert_thinfilm_thickness_ks_to_openpbr(value)
       print(f"    [CONV] Thin film thickness: {value}nm -> {converted}")
       return converted, True
   if param_name == 'thin_film_ior' and isinstance(value, (int, float)):
       converted = _convert_thinfilm_ior_ks_to_openpbr(value)
       print(f"    [CONV] Thin film IOR: {value} -> {converted}")
       return converted, True
   return value, False

def _get_node_edge_counts(node):
   try:
       in_edges = node.getInputEdges() or []
   except Exception:
       in_edges = []
   try:
       out_edges = node.getOutputEdges() or []
   except Exception:
       out_edges = []
   return len(in_edges), len(out_edges)

def _is_const_color_node(node):
   try:
       ntype = node.getType()
   except Exception:
       return False
   if isinstance(ntype, dict):
       return ntype.get("name", "") == "lux_const_color"
   return False

def _get_root_node_ids(material_graph):
   root_ids = set()
   try:
       root = material_graph.getRoot()
   except Exception:
       root = None
   if root is not None:
       try:
           root_ids.add(root.getID())
       except Exception:
           pass
   try:
       mat_roots = material_graph.getMaterialNodes() or []
   except Exception:
       mat_roots = []
   for rn in mat_roots:
       try:
           root_ids.add(rn.getID())
       except Exception:
           pass
   return root_ids

def _cleanup_material_graph(material_graph, max_passes=10):
   total_deleted = 0
   pass_index = 0
   while pass_index < max_passes:
       pass_index += 1
       zero_edge_nodes = []
       root_ids = _get_root_node_ids(material_graph)
       try:
           nodes = material_graph.getNodes()
       except Exception:
           break
       for node in nodes:
           try:
               node_id = node.getID()
           except Exception:
               continue
           if node_id in root_ids:
               continue
           if _is_const_color_node(node):
               continue
           in_count, out_count = _get_node_edge_counts(node)
           if in_count == 0 and out_count == 0:
               zero_edge_nodes.append(node)
       if not zero_edge_nodes:
           break
       for node in zero_edge_nodes:
           try:
               material_graph.removeNode(node)
               total_deleted += 1
           except Exception:
               pass
   return total_deleted

def convert_material(material_name):
   print(f"\n{'='*60}")
   print(f"  Converting: {material_name}")
   print(f"{'='*60}")

   material_graph = lux.getMaterialGraph(name=material_name)
   if not material_graph:
       print(f"  [ERROR] getMaterialGraph(name='{material_name}') failed")
       return False

   root = material_graph.getRoot()
   if not root:
       print(f"  [ERROR] getRoot() returned None")
       return False

   source, shader_type = _find_source_shader(material_graph)

   if source is None:
       openpbr_nodes = material_graph.getNodesFromType(OPENPBR_TYPE)
       if openpbr_nodes:
           print(f"  [SKIP] Already OpenPBR")
       else:
           print(f"  [SKIP] No supported shader type found")
           for node in material_graph.getNodes():
               print(f"    node: '{node.getName()}'  type: {node.getType()}")
       return False

   print(f"  Source shader: '{source.getName()}'  id: {source.getID()}")
   print(f"  Shader type: {shader_type}")

   param_map = _build_param_map(shader_type)
   extras = EXTRA_MAP.get(shader_type, {})

   print(f"\n  --- Phase 1: Reading parameters and cataloging edges ---")
   source_values = {}
   edge_reconnections = []

   for old_param, (new_param, strip) in param_map.items():
       try:
           edge = source.getInputEdge(old_param)
       except Exception:
           edge = None

       if edge:
           src_node = edge.getSourceNode()
           edge_reconnections.append((src_node, new_param, old_param))
           print(f"    [EDGE] '{old_param}' has connection -> will map to '{new_param}'")
       else:
           try:
               param = source.getParameter(old_param)
               if param is None:
                   continue
               if param.isPure():
                   print(f"    [SKIP] '{old_param}' is pure but no edge found")
                   continue
               val = param.getValue()
               if val is not None:
                   if strip:
                       val = _strip_alpha(val)
                   source_values[new_param] = val
                   print(f"    [READ] '{old_param}' = {val} -> '{new_param}'")
           except Exception as e:
               print(f"    [FAIL] '{old_param}': {e}")

   print(f"\n  --- Phase 2: Creating OpenPBR node ---")
   openpbr = material_graph.newNode(OPENPBR_TYPE)
   if openpbr is None:
       print(f"  [ERROR] newNode('{OPENPBR_TYPE}') returned None")
       return False

   print(f"  OpenPBR created: '{openpbr.getName()}'  id: {openpbr.getID()}")

   try:
       material_graph.newEdge(source=openpbr, target=root, param='surface')
       print(f"  [OK] Connected OpenPBR -> root via 'surface'")
   except Exception as e:
       print(f"  [ERROR] newEdge to root failed: {e}")
       return False

   try:
       material_graph.removeNode(source)
       print(f"  [OK] Removed old shader '{source.getName()}'")
   except Exception as e:
       print(f"  [WARN] Could not remove old shader: {e}")

   print(f"\n  --- Phase 3: Setting defaults ---")
   _set_param(openpbr, 'base_weight', 1.0)
   _set_param(openpbr, 'specular_weight', 1.0)

   for param_name, value in extras.get('fixed', {}).items():
       _set_param(openpbr, param_name, value)

   print(f"\n  --- Phase 5: Applying source values ---")
   for param_name, value in source_values.items():
       converted_value, was_converted = _apply_value_conversions(param_name, value)
       _set_param(openpbr, param_name, converted_value)

   print(f"\n  --- Phase 6: Reconnecting edges ---")
   if edge_reconnections:
       for src_node, new_param, old_param in edge_reconnections:
           try:
               material_graph.newEdge(source=src_node, target=openpbr, param=new_param)
               print(f"    [EDGE] '{old_param}' -> '{new_param}' reconnected")
           except Exception as e:
               print(f"    [FAIL] '{old_param}' -> '{new_param}': {e}")
   else:
       print(f"    No edges to reconnect.")

   print(f"\n  [DONE] {material_name} -> OpenPBR")
   return True

def display_conversion_mode_dialog():
   mode_options = [
       "All Materials in Scene",
       "Select Individual Material",
   ]
   values = [
       ("mode", lux.DIALOG_ITEM, "Conversion Mode:", mode_options[0], mode_options),
   ]
   result = lux.getInputDialog(
       title=f"OpenPBR Converter v{VERSION}",
       desc="Choose how to convert materials to OpenPBR:\n"
            "All Materials: Convert every material in the scene.\n"
            "Individual: Pick one material to convert.",
       values=values,
       id="openpbr_converter_mode.v050"
   )
   if not result:
       return None
   return result["mode"][0]

def display_material_selection():
   scene_materials = lux.getSceneMaterials()
   if not scene_materials:
       print("[ERROR] No materials found in scene.")
       return None
   values = [
       ("material", lux.DIALOG_ITEM, "Material to convert:", scene_materials[0], scene_materials),
   ]
   result = lux.getInputDialog(
       title=f"OpenPBR Converter v{VERSION}",
       desc="Select one material to convert to OpenPBR (lux_openpbr).\n"
            "Texture and utility node connections will be preserved.",
       values=values,
       id="openpbr_converter.v050"
   )
   if not result:
       return None
   return scene_materials[result["material"][0]]

def main():
   print(f"\n*** OpenPBR Material Converter v{VERSION} ***\n")

   if not lux.hasContents():
       print("[ERROR] No scene content loaded.")
       return

   mode = display_conversion_mode_dialog()
   if mode is None:
       print("[CANCELLED] No mode selected.")
       return

   materials_to_convert = []

   if mode == 0:
       all_materials = lux.getSceneMaterials()
       if not all_materials:
           print("[ERROR] No materials found in scene.")
           return
       materials_to_convert = all_materials
       print(f"\n[MODE] Converting ALL {len(materials_to_convert)} materials in scene\n")

   elif mode == 1:
       material_name = display_material_selection()
       if not material_name:
           print("[CANCELLED] No material selected.")
           return
       materials_to_convert = [material_name]
       print(f"\n[MODE] Converting individual material: {material_name}\n")

   success = 0
   fail = 0

   for material_name in materials_to_convert:
       if convert_material(material_name):
           success += 1
       else:
           fail += 1

   lux.sync()

   print(f"\n{'='*60}")
   print(f"  CLEANUP PHASE: Removing orphaned nodes")
   print(f"{'='*60}")

   cleanup_total = 0
   for material_name in materials_to_convert:
       try:
           material_graph = lux.getMaterialGraph(name=material_name)
           if material_graph:
               deleted = _cleanup_material_graph(material_graph)
               if deleted > 0:
                   print(f"  '{material_name}': Removed {deleted} orphaned node(s)")
               cleanup_total += deleted
       except Exception as e:
           print(f"  [WARN] Could not cleanup '{material_name}': {e}")

   if cleanup_total > 0:
       print(f"\n  Total orphaned nodes removed: {cleanup_total}")
   else:
       print(f"\n  No orphaned nodes found.")

   lux.sync()

   print(f"\n{'='*60}")
   print(f"  CONVERSION SUMMARY")
   print(f"{'='*60}")
   print(f"  Successful conversions: {success}")
   print(f"  Failed/skipped: {fail}")
   print(f"  Total materials: {success + fail}")
   print(f"  Orphaned nodes cleaned: {cleanup_total}")
   print(f"  Version {VERSION}")
   print(f"{'='*60}\n")

   if fail == 0:
       print(f"[SUCCESS] All {success} material(s) converted successfully!")
   else:
       print(f"[PARTIAL] {success} converted, {fail} failed/skipped.")

main()
