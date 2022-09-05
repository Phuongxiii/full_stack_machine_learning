import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 as cv 

model = tf.keras.models.load_model('../data/saved_model/my_model')
model.summary()

image = cv.imread("../data/words/a02/a02-000/a02-000-00-02.png")
img = np.invert(np.array(image))
result = model.predict(img)
