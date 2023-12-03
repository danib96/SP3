import subprocess as sp

###this first part of the script it's just to get the requested files
def change_res(input,width, height):
    output='bbb'+str(width)+'x'+str(height)+'.mp4'
    resolution = [
        'ffmpeg',
        '-i', input,
        '-vf', f'scale={width}:{height}',
        output
    ]
    sp.run(resolution)
change_res('big_buck_bunny.mp4', 360,240)
change_res('big_buck_bunny.mp4',  160,120)
change_res('big_buck_bunny.mp4',  1080,720)
change_res('big_buck_bunny.mp4',  640,480)

####this is the class of the first exercise
class codecs:
    def vp9_conv(input):
        vp9=[
        'ffmpeg',
        '-i',input,
        '-c:v','libvpx-vp9',
        '-b:v','2M',
        'vp9encoded.webm'
        ]
        sp.run(vp9)
    def vp8_conv(input):
        vp8=[
        'ffmpeg',
        '-i',input,
        '-c:v','libvpx',
        '-b:v','1M',
        '-c:a','libvorbis',
        'vp8encoded.webm'
        ]
        sp.run(vp8)
    def av1_conv(input):
        av1=[
        'ffmpeg',
        '-i',input,
        '-c:v','libaom'
        '-av1','-crf',
        '30', 'av1coded.mkv'
        ]
        sp.run(av1)
    def h625_conv(input):
        h625=[
        'ffmpeg',
        '-i',input,
        '-c:v','libx265',
        '-crf','26',
        '-preset','fast',
        '-c:a','aac',
        '-b:a','128k',
        'h625converted.mp4'
        ]
        sp.run(h625)

codecs.h625_conv('bbb1080x720.mp4')
codecs.vp8_conv('bbb160x120.mp4')
codecs.vp9_conv('bbb360x240.mp4')
codecs.av1_conv('bbb640x480.mp4')

###this is the function for exercise2
def twovideos_onscreen(input_video1, input_video2):
    compare = [
        'ffmpeg',
        '-i', input_video1,
        '-i', input_video2,
        '-filter_complex', f'blend=all_mode=difference',
        '-crf', f'18',
        'video_compare.mp4'
    ]

    sp.run(compare)
twovideos_onscreen('vp8encoded.webm','vp9encoded.webm')