import cv2
import numpy as np
import math
cap=cv2.VideoCapture("raw_front.avi")
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (800,800))

while True:
        ret,frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower = np.array([0,0,0])
        upper = np.array([190,255,20])
        mask = cv2.inRange(hsv,lower,upper)
       
        vertices= np.array([[200,550],[200,550],[370,400],[400,400],[600,550],[600,550]])
        b = cv2.fillPoly(mask, [vertices],190)
        #radius=(math.sqrt((600*600-200*200))*0.3)/70
        center = (600/2-200/2)
        #cv2.putText(mask, "Mean Radius(in m):"+str(radius),(0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
               
        edges=cv2.Canny(b,600,750)
       
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 180,50,20)
      
        for line in lines:
                coords = line[0]
                
 
        
        diff = center-abs(coords[2]-coords[0])
        imshape = mask.shape
       
        lower_left = [imshape[1]/9,imshape[0]]
        lower_right = [imshape[1]-imshape[1]/9,imshape[0]]
        top_left = [imshape[1]/2-imshape[1]/8,imshape[0]/2+imshape[0]/10]
        top_right = [imshape[1]/2+imshape[1]/8,imshape[0]/2+imshape[0]/10]
        radius = (math.sqrt((lower_right[0]*lower_right[0]-lower_left[0]*lower_left[0]))*0.3)/70
        cv2.putText(mask, "Mean Radius(in m):"+str(radius-diff*0.3/70),(0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
     
        
    
     
        
        class Car(object):
                def __init__(self):
                        self.x=0.0
                        self.y=0.0
                def value(self, val):
                        if(val<175):
                                print("gO RIGHT")
        TARGET = 175
        KP=0.02        
        x_error=0.0
        cX=diff
        car = Car()
        while x_error!=0:
                x_error = TARGET-diff
                cX +=x_error*KP
                X = max(min(1, cX),0)
                car.value(cX)      
        if (diff-175==0):
            cv2.putText(mask, "Center",(650,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
            cv2.imshow("a",mask)
            out.write(frame)
        if  diff>180:
            cv2.putText(mask, "Left",(650,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
            cv2.imshow("a",mask)
            out.write(frame)
        if diff<0:
            cv2.putText(mask, "Right",(650,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
            cv2.imshow("a",mask)
            out.write(frame)
   
        frame = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("Effect", frame)
        out.write(frame)
        k = cv2.waitKey(20)&0xff
        if k==27:
            break
out.release()
cv2.destroyAllWindows()

