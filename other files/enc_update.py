import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time


def take_img():
    cam = cv2.VideoCapture(1)
    detector = cv2.CascadeClassifier('encodings.pickle')
    Enrollment = txt.get()
    Name = txt2.get()
    sampleNum = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder
            cv2.imwrite("TrainingImage/ " + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])
            cv2.imshow('Frame', img)
        # wait for 100 miliseconds
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 100
        elif sampleNum > 70:
            break
    cam.release()
    cv2.destroyAllWindows()
    ts = time.time()
    Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    row = [Enrollment, Name, Date, Time]
    with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(row)
        csvFile.close()

