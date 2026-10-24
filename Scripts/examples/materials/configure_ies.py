"""Set RGB and IES path on one explicitly identified IES shader after preflight.

Repairs the historical conditional-precedence defect and cross-node color/file
selection. Uses existing graph nodes; does not create nodes, import libraries,
log to files or add GUI. Set MATERIAL_NAME, NODE_ID (from report_parameters.py)
and the requested IES_PATH. Dry-run defaults True. A setter exception may leave
partial changes; this is not a transaction. RGB values use the documented RGB
ShaderParameter contract, not ColorParameter.setRGBA's 0..255 contract.
Evidence: getMaterialGraph, MaterialGraph.getNodesFromType, SHADER_TYPE_IES_LIGHT,
ShaderNode.getID/getParameter, ShaderParameter.isPure/getType/setValue.
Documentation/mocked preconditions only; runtime and visible light untested.
"""
import math
from pathlib import Path
import lux

MATERIAL_NAME = ''
NODE_ID = None
IES_PATH = ''
RGB = (1.0,1.0,1.0)
DRY_RUN = True

def configure(material_name, node_id, rgb, ies_path, *, dry_run=True):
    if not isinstance(material_name,str) or not material_name.strip() or node_id is None:
        raise ValueError('Provide the exact registered material name and observed shader node ID.')
    if not isinstance(rgb,(list,tuple)) or len(rgb)!=3 or any(
        type(v) not in (int,float) or not math.isfinite(v) or not 0<=v<=1 for v in rgb):
        raise ValueError('RGB must contain exactly three finite numbers in 0..1.')
    if not ies_path:raise ValueError('Provide the requested IES file.')
    path=Path(ies_path).expanduser().resolve()
    if path.suffix.lower()!='.ies' or not path.is_file():raise ValueError('IES file must exist.')
    graph=lux.getMaterialGraph(material_name)
    if graph is None:raise ValueError('Material graph not found.')
    matches=[n for n in graph.getNodesFromType(lux.SHADER_TYPE_IES_LIGHT) if n.getID()==node_id]
    if len(matches)!=1:raise ValueError('Expected exactly one IES shader with the requested ID.')
    node=matches[0]
    color=node.getParameter('color');file_parameter=node.getParameter('file')
    for label,parameter,expected_type in [
        ('color',color,lux.PARAMETER_TYPE_COLOR),('file',file_parameter,lux.PARAMETER_TYPE_STRING)]:
        if parameter is None or parameter.isPure() or parameter.getType()!=expected_type:
            raise ValueError('Missing/pure/type-mismatched IES parameter: '+label)
    print('IES shader:',node_id,'; RGB:',tuple(rgb),'; file:',path,'; dry_run=',dry_run)
    if dry_run:return
    file_parameter.setValue(str(path))
    color.setValue(tuple(rgb))

if __name__=='__main__':configure(MATERIAL_NAME,NODE_ID,RGB,IES_PATH,dry_run=DRY_RUN)
