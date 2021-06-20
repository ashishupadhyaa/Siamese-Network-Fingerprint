from keras import backend as K
from keras.models import load_model
# K.set_image_data_format('channels_first')
from keras.optimizers import RMSprop
import numpy as np
import cv2
import os
from .block_model import model


def contrastive_loss_with_margin(margin):
  def contrastive_loss(y_true, y_pred):
    square_pred = K.square(y_pred)
    margin_square = K.square(K.maximum(margin - y_pred, 0))
    return K.mean(y_true * square_pred + (1 - y_true) * margin_square)
  return contrastive_loss


def model_l():
  mode = model((96, 96, 3))
  mode.load_weights('bioDetail/model_siamese_net1_r.h5') #Put your model name here.
  mode.compile(loss=contrastive_loss_with_margin(2), optimizer=RMSprop())
  return mode

def calculate_dist(img1, img2):
  return np.linalg.norm(img1 - img2)

def get_feature(img):
  siam_model = model_l()
  encode = siam_model.predict(np.expand_dims(img, 0))
  return encode

def img_ready(img_path):
  img = cv2.imdecode(np.frombuffer(img_path, np.uint8), -1)
  img = cv2.resize(img, (96, 96))/255.0
  img = np.around(img, decimals=6)
  return img

def calc_dist(feat_dic, img_encode):
  m_user = None
  for user, feat in feat_dic.items():
    dist = calculate_dist(feat, img_encode)

    if dist < 0.16:
      m_user = user

  return m_user
