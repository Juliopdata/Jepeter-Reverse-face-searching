import numpy as np
import cv2
def load_dataset(path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img_data_list=[]       
    input_img=cv2.imread(path)
    input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(input_img, 1.1, 3)
    x,y,w,h = faces[0]
    face = input_img[y:y+h,x:x+w]
    face=cv2.resize(face,(128,128))
    img_data_list.append(face)
    img_data = np.stack(img_data_list).astype('uint8')
    print("New photo loaded")
    return img_data/ 255.0 - 0.5