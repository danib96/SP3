import subprocess as sp
import numpy as np
import cv2
def show_2_videos(first_video,second_video):
    names = [first_video,second_video]
    window_titles = ['first', 'second']


    cap = [cv2.VideoCapture(i) for i in names]

    frames = [None] * len(names)
    gray = [None] * len(names)
    ret = [None] * len(names)

    while True:

        for i,c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read()


        for i,f in enumerate(frames):
            if ret[i] is True:
                gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                cv2.imshow(window_titles[i], gray[i])

        if cv2.waitKey(1) & 0xFF == ord('q'):
           break


    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()

####comparing the file we can see that the vp8 is the one with lower resolution, also just looking at the file size, however between the vp8 and vp9 the difference
#### is not very noticeable
