import subprocess as sp
def change_res(input,width, height):
    output='bbb'+str(width)+'x'+str(height)+'.mp4'
    resolution = [
        'ffmpeg',
        '-i', input,
        '-vf', f'scale={width}:{height}',
        output
    ]
    sp.run(resolution)