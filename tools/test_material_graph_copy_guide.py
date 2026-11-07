"""Offline contract tests for the guide's read-only helper, NOT KeyShot tests."""
import contextlib
import io
from pathlib import Path
import re
import sys
import types
import unittest
from unittest.mock import patch


GUIDE = (Path(__file__).resolve().parents[1] / 'AI' / 'kpsa_knowledge' /
         'KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt')
BLOCKS = re.findall(r'```python\n(.*?)\n```', GUIDE.read_text(encoding='utf-8'), re.S)
HELPER = next(block for block in BLOCKS if 'def verify_copy(' in block)


class Parameter:
    def __init__(self, name): self.name = name
    def getName(self): return self.name


class Node:
    def __init__(self, nid, shader_type, name):
        self.nid, self.shader_type, self.name = nid, shader_type, name
        self.inputs, self.outputs, self.slots = [], [], {}
    def getID(self): return self.nid
    def getName(self): return self.name
    def getType(self): return {'name': self.shader_type, 'display_name': 'Fixture'}
    def getInputEdges(self): return list(self.inputs)
    def getOutputEdges(self): return list(self.outputs)
    def getParameters(self): return [Parameter(name) for name in self.slots]
    def getInputEdge(self, parameter): return self.slots.get(parameter)


class Edge:
    def __init__(self, eid, source, target, parameter, enabled=True):
        self.eid, self.source, self.target = eid, source, target
        self.parameter, self.enabled = parameter, enabled
        source.outputs.append(self)
        target.inputs.append(self)
        target.slots[parameter] = self
    def getID(self): return self.eid
    def getSourceNode(self): return self.source
    def getTargetNode(self): return self.target
    def isEnabled(self): return self.enabled
    def remove(self):
        self.source.outputs.remove(self)
        self.target.inputs.remove(self)
        del self.target.slots[self.parameter]


class Graph:
    def __init__(self, offset):
        # Empty roots and duplicate shader labels are intentional.
        specs = [('root', ''), ('surface', 'duplicate'), ('noise', ''),
                 ('noise', ''), ('texture', 'duplicate'), ('noise', '')]
        self.nodes = [Node(offset + i, kind, name) for i, (kind, name) in enumerate(specs)]
        root, surface, noise_a, noise_b, texture, _detached = self.nodes
        self.edges = [Edge(offset + 100, surface, root, 'fixture_surface'),
                      Edge(offset + 101, noise_a, surface, 'fixture_color'),
                      Edge(offset + 102, noise_b, surface, 'fixture_roughness'),
                      Edge(offset + 103, texture, noise_a, 'fixture_value', False)]
        self.roots = [root]
        self.primary = root
    def getNodes(self): return list(self.nodes)
    def getRoot(self): return self.primary
    def getMaterialNodes(self): return list(self.roots)
    def getNodeFromID(self, id): return next((n for n in self.nodes if n.nid == id), None)


class CopyGuideTests(unittest.TestCase):
    def setUp(self):
        fake_lux = types.ModuleType('lux')
        fake_lux.isHeadless = lambda: True
        namespace = {'__name__': 'guide_under_test'}
        with patch.dict(sys.modules, {'lux': fake_lux}):
            exec(compile(HELPER, str(GUIDE), 'exec'), namespace)
        self.capture = namespace['capture_graph']
        self.verify = namespace['verify_copy']
        self.source, self.target = Graph(10), Graph(1000)
        # The fixture constructor knows actual correspondence. Production code
        # must obtain it while copying; list-order inference is not supported.
        self.mapping = {10 + i: 1000 + i for i in range(6)}
        with contextlib.redirect_stdout(io.StringIO()):
            self.before = self.capture(self.source)

    def result(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return self.verify(self.before, self.target, self.mapping)

    def test_python_blocks_parse(self):
        for block in BLOCKS:
            compile(block, str(GUIDE), 'exec')

    def test_blank_duplicate_names_and_new_ids(self):
        self.assertTrue(self.result())

    def test_copy_of_copy_uses_fresh_map(self):
        self.assertTrue(self.result())
        with contextlib.redirect_stdout(io.StringIO()):
            next_source = self.capture(self.target)
            self.assertTrue(self.verify(next_source, Graph(9000),
                                        {1000 + i: 9000 + i for i in range(6)}))
            with self.assertRaisesRegex(ValueError, 'every source node'):
                self.verify(next_source, Graph(9000), self.mapping)

    def test_multiple_roots_shared_node_and_different_root_order(self):
        for graph, offset in ((self.source, 10), (self.target, 1000)):
            another_root = Node(offset + 6, 'root', '')
            another_surface = Node(offset + 7, 'surface', 'duplicate')
            graph.nodes.extend((another_root, another_surface))
            graph.roots.append(another_root)
            Edge(offset + 104, another_surface, another_root, 'fixture_surface')
            Edge(offset + 105, graph.nodes[2], another_surface, 'fixture_color')
        self.target.roots.reverse()
        self.mapping.update({16: 1006, 17: 1007})
        with contextlib.redirect_stdout(io.StringIO()):
            self.before = self.capture(self.source)
        self.assertTrue(self.result())

    def test_missing_connection(self):
        self.target.edges[1].remove()
        with self.assertRaisesRegex(ValueError, 'connections differ'): self.result()

    def test_wrong_same_named_source(self):
        edge = self.target.edges[1]
        edge.source.outputs.remove(edge)
        edge.source = self.target.nodes[3]  # Same name AND shader type, different ID.
        edge.source.outputs.append(edge)
        with self.assertRaisesRegex(ValueError, 'connections differ'): self.result()

    def test_wrong_target_input(self):
        edge = self.target.edges[1]
        del edge.target.slots[edge.parameter]
        edge.parameter = 'fixture_wrong_input'
        edge.target.slots[edge.parameter] = edge
        with self.assertRaisesRegex(ValueError, 'connections differ'): self.result()

    def test_changed_enabled_state(self):
        self.target.edges[3].enabled = True
        with self.assertRaisesRegex(ValueError, 'connections differ'): self.result()

    def test_missing_reciprocal_output(self):
        edge = self.target.edges[1]
        edge.source.outputs.remove(edge)
        with self.assertRaisesRegex(ValueError, 'inventories disagree'): self.result()

    def test_ambiguous_input(self):
        edge = self.target.edges[1]
        edge.target.slots['fixture_alias'] = edge
        with self.assertRaisesRegex(ValueError, 'Unresolved target input'): self.result()

    def test_stale_source_ids(self):
        for node in self.source.nodes: node.nid += 10000
        with self.assertRaisesRegex(ValueError, 'stale'): self.result()

    def test_incomplete_map_including_detached_node(self):
        del self.mapping[15]
        with self.assertRaisesRegex(ValueError, 'every source node'): self.result()

    def test_many_to_one_map(self):
        self.mapping[12] = self.mapping[13]
        with self.assertRaisesRegex(ValueError, 'one-to-one'): self.result()

    def test_unaccounted_destination_node(self):
        self.target.nodes.append(Node(9999, 'noise', ''))
        with self.assertRaisesRegex(ValueError, 'every destination node'): self.result()

    def test_root_correspondence(self):
        self.target.roots = [self.target.nodes[1]]
        with self.assertRaisesRegex(ValueError, 'material roots differ'): self.result()

    def test_wrong_shader_type(self):
        self.target.nodes[2].shader_type = 'different_shader'
        with self.assertRaisesRegex(ValueError, 'shader types differ'): self.result()

    def test_source_is_destination(self):
        self.target = self.source
        self.mapping = {10 + i: 10 + i for i in range(6)}
        with self.assertRaisesRegex(ValueError, 'same graph'): self.result()


if __name__ == '__main__':
    unittest.main(verbosity=2)
