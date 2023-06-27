import cv2
import face_recognition
import pickle
import os


path = 'attendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is None:
       print('Wrong path:', path)
    else:
       img = cv2.resize(curImg, dsize=(128,128))
    
       images.append(curImg)
       classNames.append(os.path.splitext(cl)[0])
print(classNames)




def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        
        encodeList.append(encode)
    return encodeList

knownFace =findEncodings(images)
import pickle

filename = "known_face_encodings.pickle"
with open(filename, 'wb') as handle:
    pickle.dump(knownFace, handle, protocol=pickle.HIGHEST_PROTOCOL)

filename = "class_names.pickle"
with open(filename, 'wb') as handle:
    pickle.dump(classNames, handle, protocol=pickle.HIGHEST_PROTOCOL)
