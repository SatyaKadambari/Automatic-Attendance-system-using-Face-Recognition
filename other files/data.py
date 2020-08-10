import cv2
import os
from GUI import *

def take_img():          
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #Enrollment = num
    Name = txt.get()
    i=0
    path='dataset/'+Name+'/'
    if not os.path.exists(path):
        os.mkdir(path)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample number
            i=i+1
            # saving the captured face in the dataset folder
            cv2.imwrite(path+'data{}.jpg'.format(i),gray[y:y + h, x:x + w])
            cv2.imshow('Frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif i>100:
            break
    cam.release()
    cv2.destroyAllWindows()
