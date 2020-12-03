"""
Created For Robomaster
@Author:Wang From GDIMS
Environment:python==3.6.8 opencv==2.4.1
Date:2020/12/3
"""
import cv2
import numpy as np
from cv2 import moments
import imutils

#cap=cv2.VideoCapture(0)
image = cv2.imread(r'C:\Users\Tao\Desktop\test.jpg', 1)
while(1):
    cv2.imshow('ys',image)
    #ret,image = cap.read()
    #hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,th = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

    B,G,R = cv2.split(image)
    zeros = np.zeros(image.shape[:2],dtype="uint8")
    sub=cv2.subtract(B,G)
    cv2.imshow('gray',gray)
    cv2.imshow('sub',sub)
    cv2.imshow('th',th)
    ret,th2=cv2.threshold(sub,130, 255, cv2.THRESH_BINARY)
    cv2.imshow('th2',th2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 10))
    dilated = cv2.dilate(th2,kernel)      #膨胀图像
    max_color = th & dilated
    dilated2 = cv2.dilate(max_color,kernel)
    cv2.imshow('pz2',dilated2)
    h=cv2.findContours(dilated2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = h[0]

    cnts = imutils.grab_contours(h)
    for c in cnts:
        M=cv2.moments(c)
        area=cv2.contourArea(c)
        if area<2000 and area>500:
            rect = cv2.minAreaRect(c)
            if   0.6>rect[1][1]/rect[1][0]>0.3:
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
            if rect[2]>-45:
                box2 = cv2.boxPoints(rect)
                box2 = np.int0(box2)
                cv2.drawContours(image, [box2], -1, (0, 255, 0), 3)
                #cv2.drawContours(image,cnt,-1,(0,255,0),3)
    #hcx=int(M['m10']/M['m00'])
    #cy=int(M['m01']/M['m00'])
    #print("坐标")
    #print(cx)
    #print(cy)
    k=cv2.waitKey(5)&0xFF
    if k==17:
        break
cv.destoryAllWindows()