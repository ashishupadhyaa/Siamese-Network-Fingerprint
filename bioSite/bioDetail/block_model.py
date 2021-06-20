import tensorflow as tf
import numpy as np
import os
from keras import backend as K
from keras.layers import Conv2D, Dropout, Input
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import MaxPooling2D
from keras.layers.core import Flatten, Dense
from keras import Sequential

def model(input_shape):
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
  model.add(MaxPooling2D())
  model.add(BatchNormalization())
  model.add(Dropout(0.4))
  model.add(Conv2D(64, (3, 3), activation='relu'))
  model.add(MaxPooling2D())
  model.add(BatchNormalization())
  model.add(Dropout(0.6))
  model.add(Flatten())
  model.add(Dense(256, activation='relu'))
  model.add(Dense(128))

  return model