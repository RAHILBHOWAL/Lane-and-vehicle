import cv2
import numpy as np
import math
class Car(object):
    def __init__(self):
        self.x=0.0
        self.y=0.0
        
    def value(self, val):
        if(val<175.0):
            print(val)
            print("gO RIGHT")


while True:
    cap = cv2.VideoCapture("raw_front.avi")
    TARGET = 175.0
    KP=0.02
    car = Car()
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,0])
    upper = np.array([190,255,20])
    mask = cv2.inRange(hsv,lower,upper)
           
    vertices= np.array([[200,550],[200,550],[370,400],[400,400],[600,550],[600,550]])
    b = cv2.fillPoly(mask, [vertices],190)

    center = (600/2-200/2)

           
         
    imshape = mask.shape
           
    lower_left = [imshape[1]/9,imshape[0]]
    lower_right = [imshape[1]-imshape[1]/9,imshape[0]]
    top_left = [imshape[1]/2-imshape[1]/8,imshape[0]/2+imshape[0]/10]
    top_right = [imshape[1]/2+imshape[1]/8,imshape[0]/2+imshape[0]/10]
    radius = (math.sqrt((lower_right[0]*lower_right[0]-lower_left[0]*lower_left[0]))*0.3)/70
           
         
            
        
         
    edges=cv2.Canny(b,600,750)
           
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 180,50,20)
          
    for line in lines:
        coords = line[0]
                    
 
    diff=[]
    diff.append(center-abs(coords[2]-coords[0]))
    cX =coords[2]-coords[0]
    while True:
        for diffs in diff:
            x_error = TARGET-diffs
            cX+=x_error*KP
            X = max(min(1, cX),0)
            car.value(cX)
        
 
        
        
            
