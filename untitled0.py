"""
In the name of god


#################

PowerOfLaziness

################# 



Created By : Sajad Alipour

COPYRIGHT@2020
"""
import cv2
import time
import pyautogui
import os


def IsInTheBaze(x,a,b):
    if(x>a and x<b):
        return True
    else:
        return False

#Delay for Movements
up=0
down=0
right=0
left=0
middle=0
TimeIntegerSimulator=7
import pyautogui

cap=cv2.VideoCapture(0)
cascPath='hand.xml'
faceCascade=cv2.CascadeClassifier(cascPath)
while(True):
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30)
            )
    
    
    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if cv2.waitKey(1) & 0xFF==ord('d'):
            print('x= ',x,' y= ',y)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            quit()
        
        
        
    cv2.imshow('PowerOfLaziness',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()