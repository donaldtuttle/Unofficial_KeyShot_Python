#!/usr/bin/env python3
"""
Offline regression tests for build_symbol_index.py and verify_symbols.py.

    python -m unittest test_kpsa_symbols.py -v

Keep the three files in one folder. The fixtures below are verbatim excerpts
of the KeyShot Studio 2026.3 beta help(lux) / help(luxmath) captures, chosen
to cover every layout the parser must handle. These are static tests in an
ordinary Python interpreter, not KeyShot runtime tests.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_symbol_index as bsi   # noqa: E402
import verify_symbols as vs        # noqa: E402

LUX_EXCERPT = r'''>>>
help(lux)


Help on built-in module lux:
NAME
    lux - The module contains various classes and functions to use for manipulating the scene and rendering images.
CLASSES
    builtins.object
        Env
        MaterialGraph
        RenderOptions
        SceneNode
        ShaderNode
    class Env(builtins.object)
     |  Env encapsulates environment settings in a clear and consise way. Get an instance of the active environment using lux.getActiveEnvironment().
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  getBrightness(self, /)
     |      Get environment brightness in the form of a float value.
     |
     |  setBrightness(...)
     |      Set environment brightness.
     |      value = Brightness value to set in the form of a float. *
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
    class MaterialGraph(builtins.object)
     |  MaterialGraph encapsulates a graph of material nodes that constitutes a material in the scene, and enables manipulation of material parameters, adding/removing material nodes, and associating them with input and output edges. Get a material graph by using lux.getMaterialGraph(name).
     |
     |  Methods defined here:
     |
     |  getNodeFromID(...)
     |      Get node of material graph specified by node ID.
     |      id = Node ID. *
     |
     |  getNodes(self, /)
     |      Get list of all material nodes of the graph. The edges are considered irrelevant in this function.
     |
     |  getNodesFromType(...)
     |      Get nodes of material graph specified by node type.
     |      type = Node type. See `lux.SHADER_TYPE_..` for possibilities. *
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
    class RenderOptions(builtins.object)
     |  RenderOptions encapsulates render options in a clear and concise way. The options can be persisted as a dictionary using getDict() and fed to RenderOptions(dict=your_dict) when employing it.
     |
     |  Get an instance of the current render options using lux.getRenderOptions().
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  setMaxSamplesRendering(...)
     |      Render until max samples is reached.
     |      samples = Maximum samples. *
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None
    class SceneNode(builtins.object)
     |  SceneNode encapsulates a node in the scene tree and enables for manipulation, such as hiding/showing, locking/unlocking, setting materials etc., and traversal of the tree. It provides a means for searching and accessing groups, objects and animations for global and local operations. Get an instance of the root of the scene tree using lux.getSceneTree().
     |
     |  Methods defined here:
     |
     |  applyTransform(...)
     |      Apply a transformation (luxmath.Matrix) to the node and its children.
     |      For example, to scale the node to 1/10 of the size:
     |        T = luxmath.Matrix().makeIdentity().scale(0.1)
     |        node.applyTransform(T)
     |      Where 'node' is your lux.SceneNode.
     |
     |      trans = The transformation (luxmath.Matrix) to apply. *
     |      absolute = Whether to make an absolute transformation instead of a relative one. Must be an object node for absolute transform. (default = False)
     |
     |  find(...)
     |      Find nodes in the subtree of this node by searching part names and material names. If no names or materials are given then it will find everything.
     |      name = Part name to search for (string/tuple/list).
     |      mat = Material name to search for (string/tuple/list).
     |      all = Match all part names or all material names (default = false).
     |
     |  getChildren(self, /)
     |      Get children of group.
     |
     |  getName(self, /)
     |      Get node name.
     |
     |  setMaterial(...)
     |      Set material of a node. If applying to a group then it will apply to all sub nodes.
     |      mat = The name of the material or multi-material to apply. It can also be an instance of lux.MultiMaterial. *
     |      link = Whether to link to the material or create a duplicate. (default = False)
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
    class ShaderNode(builtins.object)
     |  ShaderNode encapsulates a shader node as part of a material graph, and enables manipulation of material parameters. Get a shader node via a material graph instance.
     |
     |  Methods defined here:
     |
     |  getParameter(...)
     |      Get parameter with specific name of this shader node.
     |      name = Name of parameter. *
     |
     |  getParameters(self, /)
     |      Get all parameters of this shader node.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
FUNCTIONS
    createAnimation(...)
        Create a new animation and attach it to the given scene node.
        node = The lux.SceneNode to attach the animation to. *
        type = Animation type string (e.g. lux.ANIMATION_TYPE_TURNTABLE). Use one of the lux.ANIMATION_TYPE_* constants. *
        name = Optional name for the animation. Auto-generated if omitted.
    getActiveEnvironment()
        Get active environment instance for manipulating and retrieving information.
    getAnimations(...)
        Return a list of all lux.Animation objects in the scene.
        node = Optional lux.SceneNode to restrict results to direct animation children of that node. Returns all animations in the scene when omitted.
    getBrowserDialog(...)
        Deprecated and will not work in KeyShot 2024.2.
        Show browser dialog. Specify either URL or HTML contents.
        url = URL to load inside browser dialog (use 'file:///' to load local files).
        html = HTML contents to load inside browser dialog.
    getInputDialog(...)
        Show dialog according to the arguments provided and return the results. It returns None if cancelled.
        For example, to show a dialog asking a string, an integer between 10 and 50 that has default value 42, and an item of [1, 2, 3]:
            values = [("string", lux.DIALOG_TEXT, "Input string:", "hello")]
            opts = lux.getInputDialog(title = "This is the title", values = values)
        title = Title of the dialog. *
        desc = Description of dialog. (default = None)
        values = The values of the dialog to build and show. *
        id = Special ID to enable persisting values and when reopening. (default = None)
    getMaterialGraph(...)
        Get lux.MaterialGraph object representing the material graph denoted by the material name.
        name = Material name to access. *
    getRenderOptions(...)
        Returns render options as a lux.RenderOptions object. If defaults is set then it will return the internal defaults, otherwise it's the values as they appear in the render dialog.
        defaults = Return defaults or not (default = false).
    getSceneTree(...)
        Get lux.SceneNode object representing the root of the scene tree.
    isHeadless()
        Returns whether KeyShot is running in headless or GUI mode.
    renderImage(...)
        Renders the scene to an image file.
        path = File path to render to. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). *
        width = Resolution width in pixels of the output image (default = scene width).
        height = Resolution height in pixels of the output image (default = scene height).
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
        format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG (requires file extension to match).
    saveFile(...)
        Saves scene to a file. If no path is given then known path is used or a dialog will ask in GUI mode while an exception is thrown in headless mode.
        path = File to save to.
        excludeFlags = A list of properties that can be filtered out. (default = empty)
    saveMaterialMetadata(object, /)
        Persist the changes made to the metadata of a material.
        metadata = The metadata object on which the metadata properties have been updated. *
DATA
    DIALOG_TEXT = 0
    NODE_TYPE_OBJECT = 2
    RENDER_OUTPUT_JPEG = 0
    RENDER_OUTPUT_PNG = 5
    SHADER_TYPE_METAL = 'lux_metal'
FILE
    (built-in)
88ms
'''

LUXMATH_EXCERPT = r'''Help on built-in module luxmath:
NAME
    luxmath - The module contains a vector and matrix class for mathematical operations.
CLASSES
    builtins.object
        Matrix
        Vector
    class Matrix(builtins.object)
     |  Matrix enables mathematical operations of matrices and vectors.
     |
     |  Methods defined here:
     |
     |  scale(...)
     |      Scale a copy of the Matrix by a Vector or number and return the result.
     |      val = Vector or number to scale with. *
     |
     |  translate(...)
     |      Translate a copy of the Matrix by a Vector and return the result.
     |      vec = Vector to translate by. *
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  makeIdentity()
     |      Creates an identity matrix (class method).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  data
     |      The Matrix data (4x4).
    class Vector(builtins.object)
     |  Vector enables mathematical operations of vectors.
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add(...)
     |      Adds the Vector to a copy of this Vector and returns the result.
     |      vec = Vector to add. *
     |
     |  len(self, /)
     |      Returns the length of the Vector.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  x
     |      The X part.
FILE
    (built-in)
4ms
'''


def build(lux=LUX_EXCERPT, luxmath=LUXMATH_EXCERPT):
    sources = [("lux.md", lux)] + ([("luxmath.md", luxmath)] if luxmath else [])
    return bsi.build_index(sources, build="test-build")


def check(source, policy=True, strict=False, luxmath=True):
    data, problems = build(luxmath=LUXMATH_EXCERPT if luxmath else None)
    assert not problems, problems
    return vs.analyze_source(source, vs.SymbolIndex(data), "t.py", policy=policy, strict=strict)


def codes(result):
    return [f["code"] for f in result["findings"]]


class BuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index, cls.problems = build()
        cls.lux = cls.index["modules"]["lux"]
        cls.math = cls.index["modules"]["luxmath"]

    def test_self_check_passes_and_counts(self):
        self.assertEqual(self.problems, [])
        self.assertEqual(set(self.lux["classes"]),
                         {"Env", "MaterialGraph", "RenderOptions", "SceneNode", "ShaderNode"})
        self.assertIn("renderImage", self.lux["functions"])
        self.assertEqual(self.lux["constants"]["SHADER_TYPE_METAL"]["type"], "str")
        self.assertEqual(self.lux["constants"]["RENDER_OUTPUT_PNG"]["value"], "5")

    def test_truncated_capture_fails_self_check(self):
        truncated = LUX_EXCERPT.split("    class ShaderNode")[0] + "FUNCTIONS\n"
        _, problems = build(lux=truncated)
        self.assertTrue(any("ShaderNode" in p for p in problems))

    def test_docstring_parameters(self):
        p = {x["name"]: x for x in self.lux["functions"]["renderImage"]["params"]}
        self.assertTrue(p["path"]["required"])
        self.assertFalse(p["width"]["required"])
        self.assertEqual(p["width"]["default"], "scene width")
        self.assertEqual(self.lux["functions"]["renderImage"]["params_source"], "docstring")

    def test_example_code_is_not_a_parameter(self):
        apply = self.lux["classes"]["SceneNode"]["members"]["applyTransform"]
        self.assertEqual([x["name"] for x in apply["params"]], ["trans", "absolute"])
        dialog = self.lux["functions"]["getInputDialog"]
        self.assertEqual([x["name"] for x in dialog["params"]], ["title", "desc", "values", "id"])

    def test_real_signatures(self):
        self.assertEqual(self.lux["functions"]["isHeadless"]["params"], [])
        self.assertEqual(self.lux["functions"]["isHeadless"]["params_source"], "signature")
        meta = self.lux["functions"]["saveMaterialMetadata"]
        self.assertEqual(meta["params_source"], "signature")
        self.assertTrue(meta["params"][0]["positional_only"])
        get_b = self.lux["classes"]["Env"]["members"]["getBrightness"]
        self.assertEqual((get_b["params"], get_b["params_source"]), ([], "signature"))
        init = self.lux["classes"]["Env"]["members"]["__init__"]
        self.assertTrue(init["accepts_varargs"] and init["accepts_varkw"])

    def test_member_kinds(self):
        self.assertEqual(self.math["classes"]["Matrix"]["members"]["makeIdentity"]["kind"], "class")
        self.assertEqual(self.math["classes"]["Matrix"]["members"]["data"]["kind"], "attribute")
        self.assertEqual(self.lux["classes"]["RenderOptions"]["members"]["__hash__"]["value"], "None")

    def test_stated_return_types(self):
        f = self.lux["functions"]
        self.assertEqual(f["getMaterialGraph"]["returns"]["type"], "lux.MaterialGraph")
        self.assertEqual(f["getSceneTree"]["returns"]["type"], "lux.SceneNode")
        self.assertEqual(f["getActiveEnvironment"]["returns"]["type"], "lux.Env")
        self.assertIn("class docstring", f["getActiveEnvironment"]["returns"]["source"])
        self.assertEqual(f["getRenderOptions"]["returns"]["type"], "lux.RenderOptions")
        anims = f["getAnimations"]["returns"]
        self.assertEqual((anims["kind"], anims["element"]["kind"]), ("list", "undeclared"))
        m = self.math["classes"]["Matrix"]["members"]
        self.assertEqual(m["scale"]["returns"]["type"], "luxmath.Matrix")
        self.assertEqual(m["makeIdentity"]["returns"]["type"], "luxmath.Matrix")
        self.assertNotIn("returns", self.lux["classes"]["MaterialGraph"]["members"]["getNodes"])

    def test_undeclared_doc_references(self):
        refs = {r["symbol"]: r for r in self.index["doc_references"]["lux"]}
        self.assertTrue(refs["lux.ANIMATION_TYPE_"]["prefix"])
        self.assertIn("lux.ANIMATION_TYPE_TURNTABLE", refs)
        self.assertIn("lux.Animation", refs)
        self.assertNotIn("lux.SHADER_TYPE_", refs)          # SHADER_TYPE_METAL is declared
        self.assertNotIn("lux.SceneNode", refs)

    def test_flags(self):
        f = self.lux["functions"]
        self.assertTrue(f["getBrowserDialog"].get("deprecated"))
        self.assertTrue(f["getBrowserDialog"].get("gui_only"))
        self.assertTrue(f["getInputDialog"].get("gui_only"))
        self.assertIn("headless", f["saveFile"]["headless_note"])

    def test_markdown_fences_and_both_modules_in_one_file(self):
        combined = "# dumps\n```\n" + LUX_EXCERPT + "\n" + LUXMATH_EXCERPT + "```\n"
        data, problems = bsi.build_index([("both.md", combined)], build="x")
        self.assertEqual(problems, [])
        self.assertEqual(set(data["modules"]), {"lux", "luxmath"})


class CheckerTests(unittest.TestCase):
    def test_clean_script(self):
        r = check(
            "import lux\nimport luxmath\n"
            "root = lux.getSceneTree()\n"
            "for node in root.find(name='Body'):\n"
            "    node.setMaterial('Steel', link=True)\n"
            "T = luxmath.Matrix().makeIdentity().scale(0.1).translate(luxmath.Vector((1, 2, 3)))\n"
            "root.applyTransform(T, absolute=False)\n"
            "if not lux.isHeadless():\n"
            "    lux.getInputDialog(title='t', values=[('a', lux.DIALOG_TEXT, 'A', '')])\n"
            "lux.renderImage('C:/out/a.png', width=800, format=lux.RENDER_OUTPUT_PNG)\n")
        self.assertEqual(r["findings"], [])
        self.assertEqual(r["exit_code"], 0)

    def test_undeclared_module_function(self):
        r = check("import lux\nlux.renderImages('a.png')\n")
        self.assertEqual(codes(r), ["E-UNDECLARED"])
        self.assertIn("renderImage", r["findings"][0]["message"])
        self.assertEqual(r["exit_code"], 1)

    def test_typed_member_missing_and_wrong_owner(self):
        r = check("import lux\nroot = lux.getSceneTree()\nroot.getParameters()\n")
        self.assertEqual(codes(r), ["E-NO-MEMBER"])
        self.assertIn("lux.ShaderNode", r["findings"][0]["message"])

    def test_doc_only_symbol_is_probe(self):
        r = check("import lux\nroot = lux.getSceneTree()\n"
                  "lux.createAnimation(root, lux.ANIMATION_TYPE_TURNTABLE)\n")
        self.assertEqual(codes(r), ["P-DOC-ONLY"])
        self.assertEqual(r["exit_code"], 2)
        self.assertIn("hasattr(lux, _name)", r["probe_snippet"])

    def test_members_of_undeclared_type_are_probes(self):
        r = check("import lux\nfor a in lux.getAnimations():\n    a.play()\n")
        self.assertEqual(codes(r), ["P-UNDECLARED-TYPE"])
        self.assertIn("'Animation'", r["probe_snippet"])

    def test_argument_checks(self):
        r = check("import lux\nenv = lux.getActiveEnvironment()\nenv.getBrightness(2)\n")
        self.assertEqual(codes(r), ["E-ARGS"])
        r = check("import lux\nlux.isHeadless(True)\n")
        self.assertEqual(codes(r), ["E-ARGS"])
        r = check("import lux\nlux.saveMaterialMetadata(object=1)\n")
        self.assertEqual(codes(r), ["E-ARGS"])
        r = check("import lux\nlux.renderImage('a.png', resolution=(1, 2))\n")
        self.assertEqual(codes(r), ["W-ARGS"])
        r = check("import lux\nlux.renderImage(width=10)\n")
        self.assertEqual(codes(r), ["W-ARGS"])
        self.assertIn("'path'", r["findings"][0]["message"])

    def test_call_site_parameter_typing(self):
        r = check("import lux\n"
                  "def walk(node):\n"
                  "    return node.getMaterialName()\n"
                  "walk(lux.getSceneTree())\n")
        self.assertEqual(codes(r), ["E-NO-MEMBER"])

    def test_annotation_typing(self):
        r = check("import lux\n"
                  "def paint(graph: 'lux.MaterialGraph'):\n"
                  "    graph.getNodeByName('x')\n")
        self.assertEqual(codes(r), ["E-NO-MEMBER"])

    def test_untyped_lux_value(self):
        r = check("import lux\nroot = lux.getSceneTree()\n"
                  "for child in root.getChildren():\n"
                  "    print(child.getName().upper())\n"
                  "    child.explode()\n")
        self.assertEqual(codes(r), ["W-UNKNOWN-MEMBER"])

    def test_matrix_chain_stays_typed(self):
        r = check("import luxmath\nm = luxmath.Matrix().makeIdentity().scale(2).rotateXYZ(1)\n")
        self.assertEqual(codes(r), ["E-NO-MEMBER"])

    def test_imports(self):
        r = check("from lux import getSceneTree as gst, renderImagez\nroot = gst()\nroot.getName()\n")
        self.assertEqual(codes(r), ["E-UNDECLARED"])
        r = check("import lux.extras\n")
        self.assertIn("E-IMPORT", codes(r))

    def test_policy(self):
        r = check("import numpy\nimport subprocess\nimport lux\n"
                  "lux.getInputDialog(title='t', values=[])\nopen('x.txt')\n")
        got = codes(r)
        if vs.STDLIB is not None:
            self.assertIn("S-IMPORT", got)
        self.assertIn("S-SENSITIVE", got)
        self.assertIn("S-HEADLESS-GUARD", got)
        self.assertIn("S-FILE-IO", got)
        self.assertEqual(r["exit_code"], 0)
        self.assertEqual(check("import subprocess\n", strict=True)["exit_code"], 2)
        self.assertEqual(check("import subprocess\n", policy=False)["findings"], [])
        allowed = check("# kpsa: allow S-FILE-IO -- writes reports\nopen('x.txt')\n", strict=True)
        self.assertNotIn("S-FILE-IO", codes(allowed))
        self.assertEqual(allowed["exit_code"], 0)
        self.assertEqual(allowed["allowances"][0]["reason"], "writes reports")
        bare = check("# kpsa: allow S-FILE-IO\nopen('x.txt')\n")
        self.assertIn("W-ALLOW", codes(bare))
        self.assertIn("S-FILE-IO", codes(bare))
        blocked = check("# kpsa: allow E-UNDECLARED -- not a real function\n"
                        "import lux\nlux.notARealFunction()\n")
        self.assertIn("E-UNDECLARED", codes(blocked))
        self.assertIn("W-ALLOW", codes(blocked))
        self.assertEqual(blocked["exit_code"], 1)

    def test_headless_and_deprecation(self):
        r = check("import lux\nlux.saveFile()\nlux.getBrowserDialog(url='x')\n", policy=False)
        self.assertEqual(sorted(codes(r)), ["W-DEPRECATED", "W-HEADLESS"])
        self.assertEqual(check("import lux\nlux.saveFile('C:/a.bip')\n")["findings"], [])

    def test_missing_module_dump(self):
        r = check("import luxmath\nluxmath.Vector(1).nope()\n", luxmath=False)
        self.assertEqual(codes(r), ["W-NO-DUMP"])

    def test_syntax_error(self):
        r = check("import lux\nif True print(1)\n")
        self.assertEqual((r["syntax"], codes(r), r["exit_code"]), ("fail", ["E-SYNTAX"], 1))


class CommandLineTests(unittest.TestCase):
    def test_build_then_verify(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "lux.md").write_text(LUX_EXCERPT, encoding="utf-8")
            (tmp / "luxmath.md").write_text(LUXMATH_EXCERPT, encoding="utf-8")
            (tmp / "ok.py").write_text("import lux\nlux.getSceneTree().getName()\n", encoding="utf-8")
            out = tmp / "symbols.json"
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            b = subprocess.run([sys.executable, str(HERE / "build_symbol_index.py"),
                                str(tmp / "lux.md"), str(tmp / "luxmath.md"),
                                "--build", "test-build", "-o", str(out)],
                               capture_output=True, text=True, env=env)
            self.assertEqual(b.returncode, 0, b.stderr)
            self.assertEqual(json.loads(out.read_text(encoding="utf-8"))["build"], "test-build")
            v = subprocess.run([sys.executable, str(HERE / "verify_symbols.py"), str(tmp / "ok.py"),
                                "--index", str(out), "--json"],
                               capture_output=True, text=True, env=env)
            self.assertEqual(v.returncode, 0, v.stdout + v.stderr)
            self.assertEqual(json.loads(v.stdout)["results"][0]["findings"], [])


if __name__ == "__main__":
    unittest.main()
