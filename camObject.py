from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import time
from threading import *
from multiprocessing import Process
from motorObject import motor
from musicObject import music

class Camera(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.numPeople = 0
    
    def getNumPeople(self):
        return self.numPeople
    
    def setNumPeople(self,numPeople):
        self.numPeople = numPeople
    
    def run(self):
        video_captured = cv2.VideoCapture(-1)
        video_captured.release()
        video_captured = cv2.VideoCapture(-1)

        classifier = cv2.CascadeClassifier('../openCV/haarcascade_upperbody.xml')

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        while (True): #not infiniteFORLOOP
            # read frame-by-frame
            motor_step_counter = 0
            ret, frame = video_captured.read()
            
            frame = imutils.resize(frame, width=min(400, frame.shape[1]))
            
            
            (rects, weights) = hog.detectMultiScale(frame, winStride=(8, 8), padding=(16, 16), scale=1.05)
            
            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
            
            self.numPeople = len(pick)
            print("in the camera module ", self.getNumPeople())
            
            for (xA, yA, xB, yB) in pick:
                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

            cv2.imshow('Video footage', frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
            
if __name__ == '__main__':
    camObj = Camera()
    motorObj = motor()
    musicObj = music()
    
    camObj.start()
    
    t2 = Thread(target = motorObj.camMove, args=(0,camObj.getNumPeople,))
    t2.start()
    
    t3 = Thread(target = musicObj.testMusic, args=(camObj.getNumPeople,))
    t3.start()
    
    '''
    cameraProcess = Process(target = camObj.camDetect())
    cameraProcess.start()
    
    motorProcess = Process(target = motorObj.camMove(0,camObj.getNumPeople()))
    motorProcess.start()
    
    cameraProcess.join()
    motorProcess.join()
    '''
