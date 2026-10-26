# -*- coding: utf-8 -*-
"""Offline regression tests for KeyShot Information Inspector v1.2.0

Execute: python test_KeyShot_Inspector_1_2.py
No real KeyShot installation is required. This validates Python structure and
reporting behavior, NOT runtime compatibility or actual KeyShot scene results.
"""
import ast
import os
import pathlib
import importlib.util
import tempfile
import sys
import types
import unittest
from contextlib import redirect_stdout
from io import StringIO

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "KeyShot_Inspector_1_2.py"

def fake_lux(rootfolder):
    lux = types.ModuleType("lux")
    consts = [
        "NODE_TYPE_GROUP", "NODE_TYPE_OBJECT", "NODE_TYPE_ANIMATION",
        "NODE_TYPE_MODEL_SET", "NODE_TYPE_MODEL", "NODE_TYPE_CAMERA",
    ]
    for i, c in enumerate(consts, 1):
        setattr(lux, c, i)
    folder_names = [
        "FOLDER_RESOURCE_ROOT", "FOLDER_ANIMATIONS", "FOLDER_BACKPLATES",
        "FOLDER_COLORS", "FOLDER_CONFIG_ROOT", "FOLDER_DOWNLOADS",
        "FOLDER_ENVIRONMENTS", "FOLDER_EXTERNAL_PLUGIN", "FOLDER_FAVORITES",
        "FOLDER_MATERIALS", "FOLDER_MATERIAL_TEMPLATES", "FOLDER_MODELS",
        "FOLDER_SCENES", "FOLDER_SCREENSHOTS", "FOLDER_SCRIPTS", "FOLDER_TEXTURES",
    ]
    for i, c in enumerate(folder_names, 20):
        setattr(lux, c, i)
    lux.DIALOG_LABEL = 7
    lux.DIALOG_CHECK = 4
    lux.DIALOG_ITEM = 3
    lux.DIALOG_TEXT = 0
    lux.DIALOG_FOLDER = 6
    lux.META_DATA_SIMPLE = 1
    lux.META_DATA_XMP = 0
    lux.getKeyShotFolder = lambda _t: rootfolder

    class Node:
        def __init__(self, name, kind, children=()):
            self.name, self.kind, self.children = name, kind, list(children)
        def getName(self): return self.name
        def getKind(self): return self.kind
        def getChildren(self): return self.children
        def getID(self): return 42
        def getMaterial(self): return "Blue"
        def getRenderLayer(self): return "Layer1"
        def isHidden(self): return False
        def isLocked(self): return False
        def isSelected(self): return self.name == "Part"
        def isModelSet(self): return self.kind == lux.NODE_TYPE_MODEL_SET
        def getPath(self, text=False): return ("Root", self.name)
        def getTransform(self, world=False): return (1, 0, 0, 1)
        def getCenter(self, world=False): return (0, 0, 0)
        def getBoundingBox(self, world=False): return ((-1,-1,-1),(1,1,1))
        def getSelected(self): return [part]

    part = Node("Part", lux.NODE_TYPE_OBJECT)
    modelset = Node("Set A", lux.NODE_TYPE_MODEL_SET, [part])
    root = Node("Root", lux.NODE_TYPE_GROUP, [modelset])
    lux.getSceneTree = lambda: root
    lux.getSceneInfo = lambda: {"name": "Test", "numObjects": 1}
    lux.getActiveConfiguration = lambda: {"Config": "Default"}
    lux.getSceneColors = lambda: ["Red", "Blue"]
    lux.getColorways = lambda: ["CW1"]
    lux.getColorway = lambda name: types.SimpleNamespace(getColors=lambda: [("M", "R")])
    lux.getMetaData = lambda format: {"General": {"SceneName": "Test"}} if format == 1 else "<xmp>Ok</xmp>"
    lux.dumpTree = lambda: '{"tree": "mock"}'
    lux.getModelSets = lambda: ["Set A"]
    lux.getObjects = lambda: [1,2,3]
    lux.getMaterialMapping = lambda: {1: "Blue"}
    lux.getRenderLayers = lambda: ["Layer1"]
    lux.getSceneMaterials = lambda: ["Blue"]

    class Parameter:
        def __init__(self, name, pure): self.name, self.pure = name, pure
        def getName(self): return self.name
        def getDisplayName(self): return self.name.upper()
        def getType(self): return 4
        def isPure(self): return self.pure
        def getValue(self):
            if self.pure:
                raise AssertionError("getValue called on pure parameter!")
            return 0.5

    class Shader:
        def getName(self): return "Diffuse"
        def getType(self): return {"name": "lux_diffuse"}
        def getID(self): return 104
        def getParameters(self): return [Parameter("roughness", False), Parameter("bumpmap", True)]
        def getOutputEdges(self): return []

    shader = Shader()
    class Graph:
        def getMaterialName(self): return "Blue"
        def getMaterialNodes(self): return [shader]
        def getNodes(self): return [shader]
    lux.getMaterialGraph = lambda name: Graph()
    lux.getMultiMaterial = lambda name: types.SimpleNamespace(
        getActiveMaterial=lambda: "Blue Matte",
        getSubMaterials=lambda: ["Blue Matte", "Blue Gloss"])

    def simple_methods(methods):
        return types.SimpleNamespace(**{method: (lambda m=method: "value_"+m)
                                        for method in methods})
    lux.getCamera = lambda: "Camera 1"
    lux.getCameras = lambda: ["Camera 1", "Camera 2"]
    for name in ("getCameraLens", "getSphericalCamera", "getCameraPosition",
                 "getCameraDirection", "getCameraLookAt", "getCameraUp",
                 "getCameraDistance", "getCameraFieldOfView",
                 "getCameraFocalLength", "getRenderEngine", "getLightingPreset",
                 "getKeepAspectRatio", "getLockResolution", "getAnimationInfo",
                 "getAnimationTime", "getAnimationFrame", "getOS",
                 "getKeyShotVersion", "getKeyShotDisplayVersion",
                 "getActiveStudio"):
        setattr(lux, name, (lambda n=name: "mock_"+n))
    lux.getEnvironments = lambda: ["Env"]
    lux.getImageStyles = lambda: ["Photo"]
    env_methods = ["getName", "getLightingEnvironment", "getBackgroundColor",
                   "getBackplateImage", "getBrightness", "getRotation",
                   "getHeight", "getSize", "getGroundSize",
                   "getGroundReflections", "getGroundShadows",
                   "getGroundShadowsColor", "getOcclusionGroundShadows",
                   "getFlattenGround"]
    style_methods = ["getName", "getKind", "getBloom",
                     "getChromaticAberration", "getColor",
                     "getCurve", "getDenoise", "getVignette"]
    studio_methods = ["getName", "getCamera", "getEnvironment",
                      "getImageStyle", "getModelSets", "getMultiMaterials",
                      "isMultiMaterialsEnabled"]
    lux.getActiveEnvironment = lambda: simple_methods(env_methods)
    lux.getActiveImageStyle = lambda: simple_methods(style_methods)
    lux.getStudios = lambda: ["Studio A"]
    lux.getStudio = lambda name: simple_methods(studio_methods)
    lux.getRenderOptions = lambda: types.SimpleNamespace(getDict=lambda: {"render_mode": 2})
    lux.getLightingPresets = lambda: ["Product", "Interior"]
    lux.getExternalFiles = lambda: ["test.png"]
    lux.getMaterialTemplates = lambda: ["Mat Template"]
    lux.getImportOptions = lambda: {"snap_to_ground": False}
    lux.getSystemInfo = lambda: {"CPU": "mock"}
    for library in ("getLibraryMaterials", "getLibraryTextures", "getLibraryColors",
                    "getLibraryEnvironments", "getLibraryBackplates"):
        setattr(lux, library, lambda: ["sample"])
    return lux



def fake_2026(rootfolder):
    lux = fake_lux(rootfolder)
    lux.DIALOG_INTEGER = 1
    lux.IMAGE_STYLE_BASIC = 0
    lux.IMAGE_STYLE_PHOTOGRAPHIC = 1
    lux.PARAMETER_TYPE_COLOR = 13
    lux.PARAMETER_TYPE_COLORALPHA = 14
    lux.PARAMETER_TYPE_SHADERLABEL = 65538
    lux.SHADER_TYPE_COLOR_FADE = 'animation_color'
    lux.SHADER_TYPE_CURVE_FADE = 'animation_curve'
    lux.SHADER_TYPE_FUZZ = 'lux_fuzz'
    lux.SHADER_TYPE_FLAKES = 'lux_flakes'
    lux.SHADER_TYPE_BUBBLES = 'lux_bubbles'
    lux.SHADER_TYPE_DISPLACE = 'lux_displace'
    lux.getColorway = lambda name: types.SimpleNamespace(
        getName=lambda: name, getColors=lambda: [("M", "R")])
    lux.getMultiMaterial = lambda name: types.SimpleNamespace(
        getName=lambda: name, getActiveMaterial=lambda: "Blue Matte",
        getSubMaterials=lambda: ["Blue Matte", "Blue Gloss"])
    lux.getCameraPivot = lambda: (1, 2, 3)
        ["Motion"] if node.getName() == "Part" else [])
    lux.getObjectMaterial = lambda obj: (
        {n:"Blue" for n in obj} if isinstance(obj, list) else "Blue")
    lux.getSceneColor = lambda name, multi: types.SimpleNamespace(
        getName=lambda: name, isMultiColor=lambda: bool(multi),
        getColor=lambda: (0.1,0.2,0.3,1),
        getSubColors=lambda: [],
        getActiveSubColor=lambda: None)
    lux.getRenderOptions = lambda defaults=False: types.SimpleNamespace(
        getDict=lambda: {"render_mode": 2, "defaults": bool(defaults)})
    for name in ('hasContents','isSceneChanged','isCameraUnsaved',
                 'isHeadless','isPerformanceModeEnabled','isPaused',
                 'isUndoEnabled'):
        setattr(lux, name, lambda: False)
    lux.findMaterialMetadata = lambda name: types.SimpleNamespace(
        getFieldNames=lambda: ['Name','Supplier'],
        readField=lambda field: 'value-' + field)

    root = lux.getSceneTree()
    ModelClass = type(root)
    def assign_parents(node, parent=None):
        node.parent = parent
        for c in node.getChildren():
            assign_parents(c, node)
    assign_parents(root)
    ModelClass.getMetadata = lambda self: {"role":"test"} if self.name=="Part" else {}
    ModelClass.getParent = lambda self: self.parent
    ModelClass.getHidden = lambda self: []
    ModelClass.getLocked = lambda self: []
    ModelClass.getDeleted = lambda self: []
    ModelClass.isAnimation = lambda self: self.kind == lux.NODE_TYPE_ANIMATION
    # This intentionally reproduces the original model-set error if not guarded.
    def get_layer(self):
        if self.kind == lux.NODE_TYPE_MODEL_SET:
            raise RuntimeError("getRenderLayer() can only be invoked on part/group")
        return "Layer1"
    ModelClass.getRenderLayer = get_layer

    orig_graph = lux.getMaterialGraph('Blue')
    Shader = type(orig_graph.getNodes()[0])
    Graph = type(orig_graph)
    Param = type(orig_graph.getNodes()[0].getParameters()[0])
    Graph.getRoot = lambda self: self.getNodes()[0]
    Graph.getNodesFromType = lambda self,t: [
        n for n in self.getNodes() if n.getType().get('name')==t]
    Graph.getNodeFromID = lambda self,nid: next(
        n for n in self.getNodes() if n.getID()==nid)
    Graph.getEdgeFromID = lambda self,eid: None
    Shader.getInputEdges = lambda self: []
    Shader.getInputEdge = lambda self, pname: None
    Shader.getParameter = lambda self,pname: next(
        (p for p in self.getParameters() if p.getName()==pname), None)
    Param.getColor = lambda self: (0.2,0.4,0.5)
    # Basic image style raises on getColor/getCurve, which must not be invoked.
    lux.getActiveImageStyle = lambda: types.SimpleNamespace(
        getName=lambda: "Default",
        getKind=lambda: lux.IMAGE_STYLE_BASIC,
        getBloom=lambda: True, getChromaticAberration=lambda: False,
        getDenoise=lambda: True, getVignette=lambda: False,
        getColor=lambda: (_ for _ in ()).throw(RuntimeError("Basic style")),
        getCurve=lambda: (_ for _ in ()).throw(RuntimeError("Basic style")))
    lux.setCamera = lambda *a, **k: (_ for _ in ()).throw(
        AssertionError("must NEVER change active camera"))
    lux.setAnimationFrame = lambda *a, **k: (_ for _ in ()).throw(
        AssertionError("must NEVER change animation frame"))
    return lux


class InspectorV11Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.fake = fake_2026(self.temp.name)
        sys.modules["lux"] = self.fake
        self.addCleanup(lambda: sys.modules.pop("lux", None))
        spec = importlib.util.spec_from_file_location("inspector_v11_test", SOURCE)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_all_reports_fake_2026_and_no_scene_mutations(self):
        categories = self.mod.CATEGORIES
        selected = [(title, [(label, fn) for _key, label, fn, default in entries])
                    for group, title, entries in categories]
        self.mod.SETTINGS["library_metadata_name"] = "Blue"
        self.mod.SETTINGS["output_folder"] = self.temp.name
        self.mod.SETTINGS["output_base"] = "AllReports"
        self.mod.begin_trace(self.temp.name)
        opts = {"mode": [1, "Save TXT only"], "folder": self.temp.name, "name": "AllReports"}
        path, failures, completed, skipped = self.mod.stream_report(selected, opts)
        report = pathlib.Path(path).read_text(encoding="utf-8")
        self.assertEqual(failures, 0, report[-5000:])
        self.assertIn("getCameraPivot", repr(self.mod.GETTERS_2026))
        self.assertIn("Camera pivot", report)
        self.assertIn("Root label edges", report)
        self.assertIn("Potentially disconnected nodes", report)
        self.assertIn("N/A (Basic image style)", report)
        self.assertIn("REPORT END", report)
        self.assertNotIn("getRenderLayer() can only be invoked", report)

    def test_error_counter_includes_inline_errors(self):
        self.mod.begin_trace(self.temp.name)
        opts = {"mode": [1, "Save TXT only"], "folder": self.temp.name, "name": "Errors"}
        path, count, completed, skipped = self.mod.stream_report([("Check", [
            ("inline", lambda: "x: [ERROR: bad]\\ny: [ERROR: bad2]"),
            ("fine", lambda: "OK"),
            ("exception", lambda: 1 / 0)])], opts)
        txt = pathlib.Path(path).read_text(encoding="utf-8")
        self.assertEqual(count, 3)
        self.assertIn("OK", txt)


    def test_dialog_item_default_is_integer_and_animation_opt_in_exists(self):
        captured = {}
        def dialog(**kw):
            captured.update(kw)
            return None
        self.fake.getInputDialog = dialog
        result = self.mod.select_report_options()
        self.assertIsNone(result)
        values = captured["values"]
        by_key = {row[0]: row for row in values if isinstance(row[0], str)}
        individual = by_key["individual_category"]
        self.assertEqual(individual[1], self.fake.DIALOG_ITEM)
        self.assertEqual(individual[3], 0)
        self.assertEqual(len(individual[4]), len(self.mod.CATEGORIES))
        self.assertEqual(by_key["mode"][3], 2)
        animation = by_key["allow_animation_tree"]
        self.assertEqual(animation[1], self.fake.DIALOG_CHECK)
        self.assertIs(animation[3], False)
        self.assertIn("1.2.0", captured["title"])

    def test_advanced_animation_checkbox_is_reachable_through_main(self):
        self.assertFalse(self.mod.SETTINGS["allow_animation_tree"])
        dialogs = []
        def dialog(**kw):
            dialogs.append(kw)
            if len(dialogs) == 1:
                return {"individual": True, "individual_category": [9, "Animation"],
                        "mode": [1, "Save TXT only"], "folder": self.temp.name,
                        "name": "AnimCategory", "allow_animation_tree": True}
            return {"animation_tree": True}
        self.fake.getInputDialog = dialog
        self.mod.main()
        self.assertTrue(self.mod.SETTINGS["allow_animation_tree"])
        self.assertEqual(len(dialogs), 2)
        self.assertIn("1.2.0 | Animation", dialogs[1]["title"])

    def test_missing_node_metadata_does_not_abort_report(self):
        class NodeNoMetadata:
            def getName(self): return "OldBuildNode"
            def getKind(self): return self_type
            def getID(self): return 4
            def getMaterial(self): return "(none)"
            def getRenderLayer(self): return "(none)"
            def isHidden(self): return False
            def isLocked(self): return False
            def isSelected(self): return False
            def getPath(self, text=False): return ("root", "OldBuildNode")
        self_type = self.fake.NODE_TYPE_OBJECT
        result = self.mod.fmt_node(NodeNoMetadata(), 0, detail=True)
        self.assertIn("Node metadata: [ERROR:", result)
        self.assertIn("OldBuildNode", result)

    def test_shader_type_fallback_and_missing_parameter_methods(self):
        class ShaderStringType:
            def getType(self): return "lux_custom_shader"
        self.assertEqual(self.mod.type_info(ShaderStringType()),
                         ("lux_custom_shader", "lux_custom_shader"))
        class ParamWithoutPure:
            def getValue(self):
                raise AssertionError("getValue must not be called when purity is unknown")
        self.assertIn("[UNREADABLE:", self.mod.parameter_value(ParamWithoutPure()))

    def test_cmf_library_lookup_requires_slow_opt_in(self):
        called = []
        self.fake.findMaterialMetadata = lambda name: called.append(name)
        self.mod.SETTINGS["library_metadata_name"] = "KnownLibMaterial"
        self.mod.SETTINGS["allow_slow"] = False
        self.mod.begin_trace(self.temp.name)
        opts = {"mode": [1, "Save TXT only"], "folder": self.temp.name, "name": "CMFSafe"}
        path, errors, count, skipped = self.mod.stream_report([
            ("Materials", [("MaterialMetadata.getFieldNames/readField (library)",
                            self.mod.material_library_metadata)])], opts)
        self.assertEqual(called, [])
        self.assertEqual(skipped, 1)
        self.assertIn("[SKIPPED SAFELY]",
                      pathlib.Path(path).read_text(encoding="utf-8"))

    def test_2026_exact_top_level_getter_inventory(self):
        docs = (HERE/"KeyShot_2026_Lux_API_Reference.txt")
        if docs.exists():
            import re
            block=docs.read_text(encoding="utf8").split("\nFUNCTIONS\n",1)[1].split("\nDATA\n")[0]
            all_get = set(re.findall(r'^    (get\w+)\(',block,re.M))
            dialogs = {"getBrowserDialog","getInputDialog","getInputDouble",
              "getInputFile","getInputFolder","getInputInt","getInputItem",
              "getInputText","getMessageBox"}
            self.assertEqual(set(self.mod.GETTERS_2026), all_get-dialogs)
        src_ast=ast.parse(SOURCE.read_text(encoding="utf8"))
        used = {n.attr for n in ast.walk(src_ast) if isinstance(n,ast.Attribute)
          and isinstance(n.value,ast.Name) and n.value.id=='lux'
          and n.attr.startswith('get')}
        # The animation crash hotfix deliberately blocks two native getters,
        # and dispatches the three basic animation GETs by validated name.
        dynamically_read = {"getAnimationInfo", "getAnimationTime"}
        self.assertEqual(set(self.mod.GETTERS_2026)-used,
                         withheld | dynamically_read)

    def test_native_animation_objects_are_never_invoked(self):
        """Even selecting both with all opt-ins enabled must not call native API."""
        triggered = []
        self.mod.SETTINGS["allow_slow"] = True
        self.mod.SETTINGS["allow_animation_tree"] = True
                self.mod.all_animation_objects),
                self.mod.node_animation_objects)]
        with tempfile.TemporaryDirectory() as td:
            self.mod.begin_trace(td)
            opts = {"mode": [1, "Save TXT only"], "folder": td,
                    "name": "BlockedNativeAnimations"}
            out, errors, completed, skipped = self.mod.stream_report(
                [("Animation", ops)], opts)
            body = pathlib.Path(out).read_text(encoding="utf-8")
            self.assertEqual(triggered, [])
            self.assertEqual(completed, 2)
            self.assertEqual(skipped, 2)
            self.assertIn("NATIVE CRASH PRECAUTION", body)

    def test_advanced_scene_animation_inspection_opt_in(self):
        calls = []
        def advanced():
            calls.append("advanced")
            return "safe graph result"
        ops = [("Scene animation-node hierarchy (advanced opt-in)", advanced)]
        with tempfile.TemporaryDirectory() as td:
            self.mod.begin_trace(td)
            opts = {"mode": [1, "Save TXT only"], "folder": td,
                    "name": "AnimationAdvanced"}
            self.mod.SETTINGS["allow_animation_tree"] = False
            path, _, _, skipped = self.mod.stream_report([("Animation", ops)], opts)
            self.assertEqual(skipped, 1)
            self.assertEqual(calls, [])
            self.mod.SETTINGS["allow_animation_tree"] = True
            path, _, _, skipped = self.mod.stream_report([("Animation", ops)], opts)
            self.assertEqual(skipped, 0)
            self.assertEqual(calls, ["advanced"])

    def test_safe_animation_status_checkpoints(self):
        with tempfile.TemporaryDirectory() as td:
            self.mod.begin_trace(td)
            result = self.mod.animation_status()
            trace = pathlib.Path(self.mod.CRASH_TRACE_PATH).read_text()
            self.assertIn("ANIMATION STATUS START: lux.getAnimationInfo()",trace)
            self.assertIn("ANIMATION STATUS END: lux.getAnimationFrame()",trace)
            self.assertIn("Animation frame",result)

    def test_no_scene_mutation_calls(self):
        src_ast=ast.parse(SOURCE.read_text(encoding="utf8"))
        forbidden = {'setAnimationFrame','newCamera','newNode',
           'newEdge','removeNode','removeEdge','setName','delete','hide',
           'show','applyTransform','setMaterial','setObjectMaterial',
           'executeGeometryNodes','sync','saveFile', 'setEnvironment',
           'setObjectMaterial', 'saveCamera', 'setImageStyle'}
        calls={n.func.attr for n in ast.walk(src_ast) if isinstance(n,ast.Call)
               and isinstance(n.func,ast.Attribute)}
        self.assertFalse(calls & forbidden, calls & forbidden)

    def test_dialog_flow_and_file_creation(self):
        steps=[]
        def dialog(*, title, values, id=None, desc=None):
            steps.append(title)
            if len(steps)==1:
                resp={cid:True for cid,name,ops in self.mod.CATEGORIES}
                resp.update({"individual":True,"mode":[1,"Save TXT only"],
                  "folder":self.temp.name, "name":"InformationTest",
                  "node_limit":100, "library_material":"Blue"})
                return resp
            return {v[0]:True for v in values if isinstance(v[0],str)
                    and len(v)==4}
        self.fake.getInputDialog=dialog
        with redirect_stdout(StringIO()):
            self.mod.main()
        path=pathlib.Path(self.temp.name)/"InformationTest.txt"
        self.assertTrue(path.is_file())
        txt=path.read_text(encoding="utf8")
        self.assertIn("KEYSHOT GET INFORMATION",txt)
        self.assertIn("REPORT END |",txt)
        self.assertEqual(len(steps),2)  # main dialog + exactly one individual picker
        trace=pathlib.Path(self.temp.name)/"KeyShot_Inspector_v1_2_0_Trace.txt"
        self.assertTrue(trace.is_file())
        self.assertIn("REPORT COMPLETE", trace.read_text(encoding="utf8"))


    def test_graph_edges_geometry_labels_and_orphans(self):
        mod = self.mod
        class Param:
            def __init__(self,name,kind): self.name,self.kind=name,kind
            def getName(self): return self.name
            def getDisplayName(self): return self.name
            def getType(self): return self.kind
            def isPure(self): return True
        class Node:
            def __init__(self,name,kind,nid):
                self.name,self.kind,self.nid=name,kind,nid
                self.out_edges=[];self.in_edges=[]
                self.pars=[]
            def getName(self): return self.name
            def getType(self): return {"name":self.kind,"display_name":self.kind}
            def getID(self): return self.nid
            def getParameters(self): return self.pars
            def getInputEdges(self): return self.in_edges
            def getOutputEdges(self): return self.out_edges
            def getInputEdge(self,pname):
                return next((e for e in self.in_edges if e.socket==pname),None)
            def getParameter(self,pname):
                return next((p for p in self.pars if p.name==pname),None)
        class Edge:
            def __init__(self,source,target,socket,eid):
                self.source,self.target,self.socket,self.eid=source,target,socket,eid
                source.out_edges.append(self);target.in_edges.append(self)
            def getID(self): return self.eid
            def getSourceNode(self): return self.source
            def getTargetNode(self): return self.target
            def isEnabled(self): return True
        root=Node('Root','__root',1)
        root.pars=[Param('geometry',65540),Param('labels',65538)]
        fuzz=Node('Fuzz','lux_fuzz',2)
        label=Node('Label','lux_diffuse',3)
        isolated=Node('Unused','lux_texture',4)
        Edge(fuzz,root,'geometry',11)
        Edge(label,root,'labels',12)
        class Graph:
            def getNodes(self): return [root,fuzz,label,isolated]
            def getMaterialNodes(self): return [root]
            def getRoot(self): return root
            def getMaterialName(self): return 'Material'
            def getNodeFromID(self,nid):
                return next(n for n in self.getNodes() if n.nid==nid)
            def getEdgeFromID(self,eid):
                return next(e for n in self.getNodes()
                            for e in n.out_edges if e.eid==eid)
            def getNodesFromType(self,t):
                return [n for n in self.getNodes() if n.kind==t]
        self.fake.getSceneMaterials=lambda:['Material']
        self.fake.getMaterialGraph=lambda name:Graph()
        self.assertIn('geometry', mod.graph_connections_detailed())
        self.assertIn('lux_fuzz',mod.geometry_node_report())
        self.assertIn('Label',mod.material_labels_report())
        orphan=mod.disconnected_shader_nodes()
        self.assertIn('Unused',orphan)
        self.assertNotIn('POTENTIALLY UNUSED: Fuzz',orphan)
        self.assertIn('getEdgeFromID',mod.graph_getter_lookup_tests())

    def test_builtin_gates_are_safe(self):
        s=self.mod
        node=self.fake.getSceneTree().getChildren()[0]
        text=s.fmt_node(node,1,detail=True)
        self.assertNotIn("getRenderLayer",text)
        self.assertIn("Node metadata",text)
        self.assertEqual(s.get_default_directory(),self.temp.name)


    def test_slow_library_getters_are_not_invoked_without_opt_in(self):
        def forbidden():
            raise AssertionError("Library getter must not load libraries")
        for name in ("getLibraryMaterials", "getLibraryTextures", "getLibraryColors",
                     "getLibraryEnvironments", "getLibraryBackplates"):
            setattr(self.fake, name, forbidden)
        self.mod.SETTINGS["allow_slow"] = False
        self.mod.SETTINGS["max_report_chars"] = 8000
        self.mod.begin_trace(self.temp.name)
        operation = next(
            (label, fn) for _key, _title, entries in self.mod.CATEGORIES
            for _opid, label, fn, _default in entries if _opid == "library")
        opts = {"mode": [1, "Save TXT only"],
                "folder": self.temp.name, "name": "NoLibraryScan"}
        path, errors, completed, skipped = self.mod.stream_report(
            [("Resource test", [operation])], opts)
        self.assertEqual((errors, completed, skipped), (0, 1, 1))
        self.assertIn("[SKIPPED SAFELY]", pathlib.Path(path).read_text())

    def test_crash_trace_keeps_last_unfinished_operation(self):
        self.mod.SETTINGS["allow_slow"] = False
        self.mod.begin_trace(self.temp.name)
        opts = {"mode": [1, "Save TXT only"],
                "folder": self.temp.name, "name": "Partial"}
        def simulate_native_failure():
            raise KeyboardInterrupt("simulated native interruption")
        with self.assertRaises(KeyboardInterrupt):
            self.mod.stream_report(
                [("Diagnostic", [("getProblem() - simulated",simulate_native_failure)])],
                opts)
        report=pathlib.Path(self.temp.name, "Partial.txt").read_text()
        trace=pathlib.Path(self.mod.CRASH_TRACE_PATH).read_text()
        self.assertIn("KEYSHOT GET INFORMATION", report)
        self.assertIn("GET START: Diagnostic :: getProblem()", trace)
        self.assertNotIn("GET END: Diagnostic :: getProblem()", trace)

    def test_scene_tree_respects_cap_and_read_only(self):
        self.mod.SETTINGS["max_scene_nodes"] = 2
        self.mod.SETTINGS["exhaustive"] = False
        self.assertEqual(len(self.mod.walk_scene()),2)


    def test_all_cameras_are_inspected_and_restored(self):
        state = {"camera": "Camera 1", "log": []}
        self.fake.getCamera = lambda: state["camera"]
        self.fake.getCameras = lambda: ["Camera 1", "Camera 2"]
        def switch(name):
            state["log"].append(name)
            state["camera"] = name
        self.fake.setCamera = switch
        self.fake.getCameraPosition = lambda: ("POSITION FOR " + state["camera"])
        self.mod.SETTINGS["allow_temporary_switch"] = True
        result = self.mod.all_saved_camera_details()
        self.assertIn("Camera 1", result)
        self.assertIn("Camera 2", result)
        self.assertIn("POSITION FOR Camera 2", result)
        self.assertEqual(state["camera"], "Camera 1")
        self.assertEqual(state["log"], ["Camera 2", "Camera 1"])

    def test_all_cameras_safely_skip_unsaved_active_camera(self):
        self.mod.SETTINGS["allow_temporary_switch"] = True
        self.fake.isCameraUnsaved = lambda: True
        self.fake.setCamera = lambda name: self.fail("Must not switch an unsaved camera")
        self.assertIn("UNSAVED changes", self.mod.all_saved_camera_details())

    def test_all_cameras_restore_on_exception(self):
        state = {"camera": "Camera 1"}
        self.fake.getCamera = lambda: state["camera"]
        self.fake.getCameras = lambda: ["Camera 1", "Camera 2"]
        def switch(name):
            state["camera"] = name
            if name == "Camera 2":
                raise RuntimeError("Switch interrupted")
        self.fake.setCamera = switch
        self.mod.SETTINGS["allow_temporary_switch"] = True
        result = self.mod.all_saved_camera_details()
        self.assertIn("Switch interrupted", result)
        self.assertEqual(state["camera"], "Camera 1")

    def test_all_environments_are_inspected_and_restored(self):
        state = {"env": "Interior"}
        self.fake.getEnvironments = lambda: ["Interior", "Exterior"]
        class Env:
            def __getattr__(self, name):
                if name == "getName":
                    return lambda: state["env"]
                return lambda: "{}@{}".format(name, state["env"])
        self.fake.getActiveEnvironment = lambda: Env()
        self.fake.setActiveEnvironment = lambda name: state.__setitem__("env", name)
        self.mod.SETTINGS["allow_temporary_switch"] = True
        result = self.mod.all_saved_environment_details()
        self.assertIn("Exterior", result)
        self.assertIn("getBrightness@Exterior", result)
        self.assertIn("getGroundShadowsColor@Exterior", result)
        self.assertEqual(state["env"], "Interior")

    def test_all_styles_avoid_photographic_getters_on_basic(self):
        state = {"style": "Basic"}
        self.fake.getImageStyles = lambda: ["Basic", "Photo"]
        class ImageStyle:
            def getName(self): return state["style"]
            def getKind(self): return (self_fake.IMAGE_STYLE_BASIC if
                                        state["style"] == "Basic" else
                                        self_fake.IMAGE_STYLE_PHOTOGRAPHIC)
            def __getattr__(self, name):
                if name in ("getColor", "getCurve") and state["style"] == "Basic":
                    raise AssertionError("Basic style photographic getter accessed")
                return lambda: "{}@{}".format(name, state["style"])
        self_fake = self.fake
        self.fake.getActiveImageStyle = lambda: ImageStyle()
        self.fake.setActiveImageStyle = lambda name: state.__setitem__("style", name)
        self.mod.SETTINGS["allow_temporary_switch"] = True
        result = self.mod.all_saved_image_style_details()
        self.assertIn("N/A (Basic style)", result)
        self.assertIn("getColor@Photo", result)
        self.assertEqual(state["style"], "Basic")

    def test_all_inspections_blocked_by_default(self):
        self.fake.setCamera = lambda _: self.fail("camera switched without permission")
        self.fake.setActiveEnvironment = lambda _: self.fail("env switched without permission")
        self.fake.setActiveImageStyle = lambda _: self.fail("style switched without permission")
        self.assertIn("[SKIPPED SAFELY]", self.mod.all_saved_camera_details())
        self.assertIn("[SKIPPED SAFELY]", self.mod.all_saved_environment_details())
        self.assertIn("[SKIPPED SAFELY]", self.mod.all_saved_image_style_details())

    def test_raw_metadata_export_preserves_formats_and_does_not_overwrite(self):
        self.mod.SETTINGS["output_folder"] = self.temp.name
        self.mod.SETTINGS["output_base"] = "MetadataScene"
        result = self.mod.export_native_scene_metadata()
        self.assertIn("saved:",result)
        for ext in (".metadata", ".xmp"):
            self.assertTrue(pathlib.Path(self.temp.name, "MetadataScene" + ext).is_file())
        result = self.mod.export_native_scene_metadata()
        self.assertTrue(len(list(pathlib.Path(self.temp.name).glob("MetadataScene*.xmp"))) >= 2)
        self.assertIn("MetadataScene",result)

    def test_exhaustive_mode_removes_caps_and_truncation(self):
        self.mod.SETTINGS.update(exhaustive=True, max_scene_nodes=1,
                                 max_report_chars=50)
        self.assertEqual(len(self.mod.walk_scene()),3)
        self.assertEqual(self.mod.safe_output("x"*5000), "x"*5000)

    def test_new_dialog_options_and_default_off(self):
        vals=[]
        def dialog(**kwargs):
            vals.extend(kwargs["values"])
            return None
        self.fake.getInputDialog = dialog
        self.mod.select_report_options()
        keyed = {x[0]: x for x in vals if isinstance(x[0],str)}
        self.assertIs(keyed["allow_temporary_switch"][3],False)
        self.assertIs(keyed["exhaustive"][3],False)
        self.assertIsInstance(keyed["individual_category"][3],int)


    def test_restore_failure_aborts_inventory(self):
        state = {"camera": "Camera 1", "log": []}
        self.fake.getCamera = lambda: state["camera"]
        self.fake.getCameras = lambda: ["Camera 1", "Camera 2", "Camera 3"]
        self.fake.isCameraUnsaved = lambda: False
        def switch(name):
            state["log"].append(name)
            if name == "Camera 1":
                raise RuntimeError("cannot restore")
            state["camera"] = name
        self.fake.setCamera = switch
        self.mod.SETTINGS["allow_temporary_switch"] = True
        result = self.mod.all_saved_camera_details()
        self.assertIn("[STOPPED] camera inventory aborted", result)
        self.assertNotIn("Camera 3:", result)
        self.assertEqual(state["camera"], "Camera 2")

    def test_field_level_trace_is_persisted(self):
        state={"env":"First"}
        self.fake.getEnvironments=lambda:["First","Second"]
        class Env:
            def getName(self):return state["env"]
            def __getattr__(self,name):return lambda:42
        self.fake.getActiveEnvironment=lambda:Env()
        self.fake.setActiveEnvironment=lambda name:state.__setitem__("env",name)
        self.mod.SETTINGS["allow_temporary_switch"]=True
        self.mod.begin_trace(self.temp.name)
        self.mod.all_saved_environment_details()
        trace = pathlib.Path(self.mod.CRASH_TRACE_PATH).read_text()
        self.assertIn("ENVIRONMENT SWITCH START: Second",trace)
        self.assertIn("GET START: Brightness",trace)
        self.assertIn("ENVIRONMENT RESTORE END: First",trace)

if __name__=="__main__":
    unittest.main(verbosity=2)
