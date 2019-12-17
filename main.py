from recomendator import recomender
import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

data = pd.read_csv('./data/photoDf.csv')
vectors = np.load('vectorsnp.npy')
names = [f for f in data.Path]
res = recomender(vectors,names,'./uploadphotos/{}.'.format())