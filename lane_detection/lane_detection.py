#!/usr/bin/env python3

import os
import cv2
import numpy as np
import time
import math



def main():
    print("Hello !!!")
    path = '/home/probook/ws_python/lane_detection/img/'
    pic = [ '/home/probook/Pictures/car01.jpeg',
            '/home/probook/Pictures/car02.jpeg',
            '/home/probook/Pictures/car03.png']
    indx = 2

    img = cv2.imread(pic[indx],cv2.IMREAD_COLOR)
    h, w, ch = img.shape
    print("W, H : " + str(w) + ", " + str(h))
    img[0:int(h/3),:,:] = [0,0,0]

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path+"gray"+str(indx)+".jpg", grayImg)

    cannyImg = cv2.Canny(grayImg, 50, 200, None, 3)
    cv2.imwrite(path+"canny"+str(indx)+".jpg", cannyImg)

    houghImg = np.copy(img)
    houghPImg = np.copy(img)

    lines = cv2.HoughLines(cannyImg, 1, np.pi / 180, 150, None, 0, 0)
    if lines is not None:
        print(type(lines))
        print(type(lines[0]))
        vTheta = []
        vTheta2 = []
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            vTheta.append(theta*180.0/np.pi)
            if theta > np.pi:
                theta = theta-np.pi
            elif theta < -np.pi:
                theta = theta+(2*np.pi)
            elif theta < 0:
                theta = theta+np.pi
            vTheta2.append(theta*180.0/np.pi)
            
            A = [[60, 65], [80, 90], [45, 70]]
            B = [[180-30, 180-45], [180-60, 180-90], [180-20, 180-45]]
            if theta*180.0/np.pi > A[indx][0] and theta*180.0/np.pi < A[indx][1]:
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                cv2.line(houghImg, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
            if theta*180.0/np.pi < B[indx][0] and theta*180.0/np.pi > B[indx][1]:
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                cv2.line(houghImg, pt1, pt2, (0,255,255), 3, cv2.LINE_AA)
                #print(rho)
                #print(theta)
        
        cv2.imwrite(path+"hough"+str(indx)+".jpg", houghImg)
    
    linesP = cv2.HoughLinesP(cannyImg, 1, np.pi / 180, 50, None, 50, 10)
    if linesP is not None:
        print(type(linesP))
        print(type(linesP[0]))
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(houghPImg, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
        cv2.imwrite(path+"houghP"+str(indx)+".jpg", houghPImg)
    
    '''
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    '''

if __name__ == "__main__":
    main()

