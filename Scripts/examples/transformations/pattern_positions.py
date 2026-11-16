"""Complete ordinary-Python position planners; no scene mutation or file I/O.

Repairs the historical grid capacity, missing pyramid height/layer-capacity,
ignored spiral direction and undefined helper problems. Coordinates are design
units, not inferred cm/mm. Y is up; circle/grid lie in XZ. These return tuples,
not KeyShot matrices. For actual placement validate target kind, pivot, space and
units, then use the separately documented transform helper. No runtime claim.
"""
import math

def _count(value,label):
    if type(value) is not int or value<1:raise ValueError(label+' must be a positive integer.')

def _length(value,label):
    if type(value) not in (int,float) or not math.isfinite(value) or value<=0:
        raise ValueError(label+' must be finite and positive.')

def grid_positions(count, rows, cols, spacing):
    for label,value in [('count',count),('rows',rows),('cols',cols)]:_count(value,label)
    _length(spacing,'spacing')
    if count>rows*cols:raise ValueError('Requested count exceeds grid capacity.')
    return [((i%cols)*spacing,0,(i//cols)*spacing) for i in range(count)]

def circle_positions(count, radius, *, clockwise=False):
    _count(count,'count');_length(radius,'radius')
    sign=-1 if clockwise else 1
    return [(radius*math.cos(sign*2*math.pi*i/count),0,
             radius*math.sin(sign*2*math.pi*i/count)) for i in range(count)]

def pyramid_positions(base_width, spacing):
    _count(base_width,'base_width');_length(spacing,'spacing')
    result=[]
    for layer,width in enumerate(range(base_width,0,-1)):
        for row in range(width):
            for col in range(width):
                result.append(((col-(width-1)/2)*spacing,layer*spacing,
                               (row-(width-1)/2)*spacing))
    return result

def spiral_positions(count, radial_step, angle_degrees, height_step, *, clockwise=False):
    _count(count,'count');_length(radial_step,'radial_step')
    for label,value in [('angle_degrees',angle_degrees),('height_step',height_step)]:
        if type(value) not in (int,float) or not math.isfinite(value):raise ValueError(label+' must be finite.')
    sign=-1 if clockwise else 1
    result=[]
    for i in range(1,count+1):
        angle=math.radians(sign*i*angle_degrees)
        result.append((i*radial_step*math.cos(angle),i*height_step,
                       i*radial_step*math.sin(angle)))
    return result

if __name__=='__main__':
    print('Square-layer pyramid:',pyramid_positions(3,1.0))
