import pandas as pd
import numpy as np
from facedetector import load_dataset
from predictor import build_encoder
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import os
import pandas as pd
import tarfile
import cv2
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from keras.callbacks import ModelCheckpoint
from align import AlignDlib
from keras.models import model_from_json
from keras.models import load_model
from PIL import Image
import re
import webbrowser


#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#import tensorflow as tf



encodetor = build_encoder((128, 128, 3), 1000)
encodetor.load_weights('./data/models/encoderweights128.h5')


def recomender(vectors,names,path):
    mod = list(vectors)
    s_N = names
    s = pd.Series(s_N)
    df=pd.DataFrame(s)
    df['Vector']=mod
    df.columns=(['name','X'])
    test_person=load_dataset(path)
    test_person_pred=encodetor.predict(test_person)
    X_missing=test_person_pred
    df["diffs"] = df["X"].apply(lambda X: np.linalg.norm(X-X_missing))
    results = df.groupby("name").agg({'diffs':'min'}).sort_values(by='diffs')
    filename = (results.index[0])
    s = "/"
    filename = re.findall("[\w\/\.\_\d]+",filename)
    filename = './data/'+s.join(filename)
    #filename = s.join(filename)
    #print(filename)
    
    #image = Image.open('{}'.format(filename))
    return webbrowser.open(filename)
    #return filename 

def clarator():
    return "static/celia2.jpg"
def demonator():
    #return webbrowser.open("./data/fidel1.jpg")
    return "static/fidel1.jpg"
