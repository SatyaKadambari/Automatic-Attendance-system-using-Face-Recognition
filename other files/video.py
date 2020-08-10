from imutils.video import VideoStream
import face_recognition
import imutils
import pickle
import time
import xlwt
import numpy as np
import cv2
from tkinter import *
from mark import *


#print("[INFO] loading encodings...")
data = pickle.loads(open("encodings.pickle", "rb").read())
l=[]
def fun():
    while True:
            vs = VideoStream(src=0).start()#cv2.VideoCapture('http://192.168.31.121:8080/shot.jpg')#VideoStream(src=0).start()
            frame = vs.read()
            
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)         
            rgb = imutils.resize(frame, width=750)      
            r = frame.shape[1] / float(rgb.shape[1])

            boxes = face_recognition.face_locations(rgb,
                    model='cnn')
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []
            for encoding in encodings:
                    matches = face_recognition.api.compare_faces(data["encodings"],
                                                     encoding, tolerance=0.479)
                    name = "Unknown"
                    if True in matches:
                            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                            counts = {}
                            for i in matchedIdxs:
                                    name = data["names"][i]
                                    counts[name] = counts.get(name, 0) + 1
                            name = max(counts, key=counts.get)
                    names.append(name)
            for ((top, right, bottom, left), name) in zip(boxes, names):
                    top = int(top * r)
                    right = int(right * r)
                    bottom = int(bottom * r)
                    left = int(left * r)
                    cv2.rectangle(frame, (left, top), (right, bottom),
                            (0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            0.75, (0, 255, 0), 2)
                    l.append(name)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == ord("q"):
                cv2.destroyAllWindows()
                break
                cv2.destroyAllWindows()
                vs.release()
            #function(l)
    lis = list(dict.fromkeys(l))
    try:
        lis.remove('Unknown')
        print(lis)
    except ValueError:
        print(lis)
    print(lis)
   

