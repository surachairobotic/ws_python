#!/usr/bin/env python3

import os
import cv2
import numpy as np
import time

def main():
    print("Hello !!!")

    cap = cv2.VideoCapture('/home/probook/Downloads/Data.mp4')
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))*1.0
    print("frame : " + str(frame_width) + " x " + str(frame_height) + ", FPS=" + str(fps))

    ms = [(1.0*x)/fps for x in range(int(fps))]
    second = 0
    minute = 0
    hr = 0
    print(ms)
    print(second)
    print(minute)

    checkpoint = time.time()
    checkpoint_frame = 0

    cnt=cnt2=0
    while True:
        if time.time()-checkpoint >= 1.0:
            checkpoint = time.time()
            print("FPS : ", cnt2-checkpoint_frame)
            cnt2=0
    
        ret, frame = cap.read()
        if frame is None:
            break
        
        cnt=(cnt+1)
        cnt2=(cnt2+1)
        if cnt >= int(fps-1):
            cnt=0
            second=second+1
            
            x = "{:2.2f}".format(ms[cnt])[2:]
            t = str(hr)+':'+"{:02d}".format(minute)+':'+"{:02d}".format(second)
            path = "/home/probook/ws_python/vdo2images/img/"+str(hr)+'/'
            if not os.path.exists(path):
                os.makedirs(path)
            cv2.imwrite(path+t+".jpg", frame)
            
            if second is 60:
                second=0
                minute=minute+1
                print(str(hr)+":"+str(minute))
                if minute is 60:
                    minute=0
                    hr=hr+1
            
        if cv2.waitKey(1) != -1:
            break

if __name__ == "__main__":
    main()

