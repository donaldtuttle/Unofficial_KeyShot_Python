"""Render held frames to unique PNG positions; encode an existing complete sequence.

All helpers are included; only standard Python and built-in lux are used.
Configure the requested existing output folder, inclusive source range and FPS.
HOLDS maps a source frame to its TOTAL copies, not extra copies. Dry-run defaults
to True. No folders are created, inputs deleted or existing outputs overwritten.
Preflight is not an atomic file reservation or rollback. Rendering can leave a
partial sequence on failure. Frame restoration is attempted in finally.
Evidence: lux.getAnimationFrame/setAnimationFrame, getRenderOptions,
RenderOptions.setAddToQueue/setSendToNetwork/setMaxSamplesRendering, renderImage,
encodeVideo. Documentation/offline checks only; KeyShot/visual tests not passed.
"""
import math
import re
from pathlib import Path
import lux

OUTPUT_FOLDER = ''
FRAME_FORMAT = 'frame.%04d.png'
START_FRAME = 1
END_FRAME = 10
OUTPUT_FIRST = 1
HOLDS = {}
WIDTH = 1920
HEIGHT = 1080
SAMPLES = 64
FPS = 10
VIDEO_NAME = 'video.mp4'
DRY_RUN = True

def positive_int(value, label, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError(label + ' must be an integer >= ' + str(minimum))

def filename_format(value):
    if not isinstance(value, str) or not value or any(c in value for c in '/\\:<>"|?*\0'):
        raise ValueError('Frame format must be a basename in the requested folder.')
    tokens=list(re.finditer(r'%(?:0[1-9][0-9]*)?d',value))
    if len(tokens)!=1 or '%' in value[:tokens[0].start()]+value[tokens[0].end():]:
        raise ValueError('Use exactly one %d or %0Nd frame placeholder.')
    token=tokens[0].group()
    if token!='%d' and int(token[2:-1])>12:
        raise ValueError('Frame padding width must not exceed 12.')
    if not value.lower().endswith('.png'):
        raise ValueError('This renderer example produces PNG frames only.')
    return value

def frame_plan(start, end, holds=None, output_first=1):
    positive_int(start,'start',0);positive_int(end,'end',0)
    positive_int(output_first,'output_first',0)
    if start>end:raise ValueError('Inclusive start must not exceed end.')
    holds={} if holds is None else holds
    if not isinstance(holds,dict):raise TypeError('holds must be a dictionary.')
    for frame,copies in holds.items():
        positive_int(frame,'held source frame',0);positive_int(copies,'total copies')
        if not start<=frame<=end:raise ValueError('Held frame is outside the source range.')
    plan=[];position=output_first
    for frame in range(start,end+1):
        for _ in range(holds.get(frame,1)):
            plan.append((frame,position));position+=1
    return plan

def folder_path(folder):
    if not folder:raise ValueError('Provide the requested existing output folder.')
    path=Path(folder).expanduser().resolve()
    if not path.is_dir():raise ValueError('Folder must already exist.')
    return path

def render_sequence(folder, fmt, start, end, holds=None, *, output_first=1,
                    width=1920, height=1080, samples=64, dry_run=True):
    folder=folder_path(folder);fmt=filename_format(fmt)
    for label,value in [('width',width),('height',height),('samples',samples)]:
        positive_int(value,label)
    plan=frame_plan(start,end,holds,output_first)
    paths=[folder/(fmt % position) for _,position in plan]
    if any(path.exists() for path in paths):
        raise FileExistsError('A planned frame destination already exists; nothing rendered.')
    print('Source frames:',start,'through',end,'; output positions:',len(plan))
    if dry_run:return plan
    previous=lux.getAnimationFrame()
    options=lux.getRenderOptions(defaults=True)
    options.setAddToQueue(False);options.setSendToNetwork(False)
    options.setMaxSamplesRendering(samples)
    try:
        for (frame,position),path in zip(plan,paths):
            if path.exists():raise FileExistsError(str(path))
            lux.setAnimationFrame(frame)
            result=lux.renderImage(path=str(path),width=width,height=height,opts=options)
            if result is False:raise RuntimeError('Render stopped at output position '+str(position))
            if not path.is_file() or path.stat().st_size==0:
                raise RuntimeError('No nonempty frame produced: '+str(path))
    finally:
        lux.setAnimationFrame(previous)
    return plan

def encode_sequence(folder, fmt, first, last, fps, video_name, *, dry_run=True):
    folder=folder_path(folder);fmt=filename_format(fmt)
    positive_int(first,'first',0);positive_int(last,'last',0)
    if first>last:raise ValueError('Inclusive first must not exceed last.')
    if type(fps) not in (int,float) or not math.isfinite(fps) or fps<=0:
        raise ValueError('FPS must be a finite positive number; it is never rounded.')
    if not isinstance(video_name,str) or any(c in video_name for c in '/\\:<>"|?*\0') or not video_name.lower().endswith('.mp4'):
        raise ValueError('Provide an MP4 basename in the frame folder.')
    output=folder/video_name
    if output.exists():raise FileExistsError(str(output))
    missing=[fmt % frame for frame in range(first,last+1)
             if not (folder/(fmt % frame)).is_file() or (folder/(fmt % frame)).stat().st_size==0]
    if missing:raise FileNotFoundError('Missing/empty expected frames: '+', '.join(missing))
    print('Encode frames:',first,'through',last,'; FPS:',fps,'; duration:',(last-first+1)/fps)
    if dry_run:return str(output)
    if output.exists():raise FileExistsError(str(output))
    result=lux.encodeVideo(folder=str(folder),frameFiles=fmt,videoName=video_name,
                           fps=fps,firstFrame=first,lastFrame=last,keepFrames=True)
    if result is False:raise RuntimeError('Encoder reported cancellation/failure.')
    if not output.is_file() or output.stat().st_size==0:
        raise RuntimeError('Encoder returned without a nonempty output; inspect KeyShot.')
    return str(output)

if __name__=='__main__':
    sequence=render_sequence(OUTPUT_FOLDER,FRAME_FORMAT,START_FRAME,END_FRAME,HOLDS,
        output_first=OUTPUT_FIRST,width=WIDTH,height=HEIGHT,samples=SAMPLES,dry_run=DRY_RUN)
    # Encoding is a separate explicit call after reviewing the produced sequence:
    # encode_sequence(OUTPUT_FOLDER,FRAME_FORMAT,sequence[0][1],sequence[-1][1],
    #                 FPS,VIDEO_NAME,dry_run=DRY_RUN)
