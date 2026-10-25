# OpenPBR and Planar Light — runtime parameters

Captured in KeyShot Studio 2026.3 beta by inspecting shader nodes on live materials. These parameters are not a separate library file. Read them from the material graph.

`SHADER_TYPE_OPENPBR` (`lux_openpbr`) and `SHADER_TYPE_PLANAR_LIGHT` (`lux_arealight`) exist in the 2026.3 beta dump. The parameter lists below come from `getParameters()` on the nodes, not from a static catalog.

Type numbers match the dump:

| Type | Constant |
| --- | --- |
| 1 | `PARAMETER_TYPE_BOOLEAN` |
| 2 | `PARAMETER_TYPE_INTEGER` |
| 4 | `PARAMETER_TYPE_FLOAT` |
| 9 | `PARAMETER_TYPE_STRING` |
| 12 | `PARAMETER_TYPE_MATRIX` |
| 13 | `PARAMETER_TYPE_COLOR` |
| 14 | `PARAMETER_TYPE_COLORALPHA` |
| 65537 | `PARAMETER_TYPE_SHADERSURFACE` |
| 65538 | `PARAMETER_TYPE_SHADERLABEL` |
| 65539 | `PARAMETER_TYPE_SHADERBUMP` |
| 65540 | `PARAMETER_TYPE_SHADERGEOMETRY` |

Type 0 appears on some tangent parameters. It is not a named constant in the dump. Do not invent a name for it.

## Planar Light

Material: `Planar Light Material`

Root node:

- geometry (65540)
- labels (65538)
- surface (65537)

Light node:

- apply_bump_to_labels (1)
- bumpmap (65539)
- diffuse (14)
- opacitymap (14)
- opacitymap_mode (2)

## OpenPBR

Material: `Mold-Tech-11030 Spray Dot OpenPBR`

Root node:

- geometry (65540)
- labels (65538)
- surface (65537)

Mapping node (triplanar-style):

- angleX, angleY, angleZ (4)
- blend (4)
- blend_color (1)
- brightness (4)
- bump_height (4)
- contrast (4)
- default_color (13)
- first_shader (14)
- flagsX, flagsY, flagsZ (2)
- normalX, normalY, normalZ (1)
- second_shader (14)
- sync (1)
- textureUseProfileX, textureUseProfileY, textureUseProfileZ (1)
- textureX, textureY, textureZ (9)
- texture_space (2)
- third_shader (14)
- transform_obj_to_uv (12)
- uScaleX, uScaleY, uScaleZ (4)
- vScaleX, vScaleY, vScaleZ (4)

OpenPBR node:

- base_color (13)
- base_diffuse_roughness (4)
- base_metalness (4)
- base_weight (4)
- coat_color (13)
- coat_darkening (4)
- coat_ior (4)
- coat_roughness (4)
- coat_roughness_anisotropy (4)
- coat_weight (4)
- emission_color (13)
- emission_luminance (4)
- fuzz_color (13)
- fuzz_roughness (4)
- fuzz_weight (4)
- geometry_coat_normal (65539)
- geometry_coat_tangent (0)
- geometry_normal (65539)
- geometry_opacity (4)
- geometry_tangent (0)
- geometry_thin_walled (1)
- specular_color (13)
- specular_ior (4)
- specular_roughness (4)
- specular_roughness_anisotropy (4)
- specular_weight (4)
- subsurface_color (13)
- subsurface_radius (4)
- subsurface_radius_scale (13)
- subsurface_scatter_anisotropy (4)
- subsurface_weight (4)
- thin_film_ior (4)
- thin_film_thickness (4)
- thin_film_weight (4)
- transmission_color (13)
- transmission_depth (4)
- transmission_disp_abbe_number (4)
- transmission_disp_scale (4)
- transmission_scatter (13)
- transmission_scatter_ani (4)
- transmission_weight (4)

## How to read them

```python
graph = lux.getMaterialGraph(name="Mold-Tech-11030 Spray Dot OpenPBR")
if graph:
    for node in graph.getNodes():
        for param in node.getParameters():
            print(param.getName(), param.getType())
```

Do not assume every OpenPBR or Planar Light graph has the same node count. Inspect the graph. Empty parameter lists in a dump mean that node had no exposed parameters at capture time.
