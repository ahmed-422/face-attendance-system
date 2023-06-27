import cv2
import numpy as np
import face_recognition
import os
from datetime import  datetime
import pickle


# to reduce wecam preview resolution

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)





def markAttendance(name):
    with open('attendance.csv', 'r+', encoding="utf8") as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

filename = "known_face_encodings.pickle"
with open(filename, 'rb') as handle:
    encodeListKnown = pickle.load(handle)


filename = "class_names.pickle"
with open(filename, 'rb') as handle:
    classNames = pickle.load(handle)



cap = cv2.VideoCapture(0)




while True:
    success, img = cap.read()
    resize = ResizeWithAspectRatio(img, width=300)
    resize = ResizeWithAspectRatio(img, height=500)
    imgS = cv2.resize(resize,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(resize,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(resize,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(resize,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)


    cv2.imshow('Webcam',resize)
    cv2.waitKey(1)





