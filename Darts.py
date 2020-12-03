"""
Created For Robomaster
@Author:Wang From GDIMS
Environment:python==3.6.8 opencv==2.4.1
Date:2020/12/3
Tips:Most of the commented statements are visual windows

This example is only for exchange and learning, 
and only for the participants of our school,
Thank you for your support
"""
import cv2
import numpy as np
from cv2 import moments
import imutils

cap=cv2.VideoCapture(1)
while(1):

    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)          #Color space conversion
    ret,th = cv2.threshold(gray,250,325,cv2.THRESH_BINARY)

    B,G,R = cv2.split(frame)
    zeros = np.zeros(frame.shape[:2],dtype="uint8")        #Separation of RGB channels

    #cv2.imshow('gray',gray)
    #cv2.imshow('sub',sub)
    #cv2.imshow('th',th)

    #cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
    #cv2.imshow("RED",cv2.merge([zeros,zeros,R]))
    sub=cv2.subtract(R,B)     #Channel subtraction, confirm color If it is changed to blue, it will be changed to sub=cv2.subtract(B,R)
    #cv2.imshow('sub',sub)
    ret,th2=cv2.threshold(sub,110, 255, cv2.THRESH_BINARY)
    #cv2.imshow('th2',th2)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 10))
    dilated = cv2.dilate(th2,kernel) 

    #cv2.imshow('pz',dilated)

    max_color = th & dilated
    dilated2 = cv2.dilate(max_color,kernel)

    h=cv2.findContours(dilated2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #Looking for contours

    cnt = h[0]
    #cv2.imshow('pz2',dilated2)
    

    cnts = imutils.grab_contours(h)
    for c in cnts:
        M=cv2.moments(c)
        area=cv2.contourArea(c)
        
        cv2.drawContours(frame,cnt,-1,(0,255,0),5)
        pt = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
        #cX = int(M["m10"] / M["m00"])
        #cY = int(M["m01"] / M["m00"])                                        #Draw the outline and center and coordinates
        cv2.circle(frame, pt, 1, (0, 0, 139), 3)
        text = "(" + str(pt[0]) + ", " + str(pt[1]) + ")"
        cv2.putText(frame, text,(pt[0]+30, pt[1]+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow('cs',frame)
        print(area)


    #hcx=int(M['m10']/M['m00'])
    #cy=int(M['m01']/M['m00'])
    #print("坐标")
    #print(cx)
    #print(cy)

    k=cv2.waitKey(5)&0xFF
    if k==17:
        break
cv.destoryAllWindows()