# File: predict.py
# 
# Description: Provides functions to receive an image as input, preprocess it,
# and predict whether or not the image represents something edible.
#
# Author: Dan Johnson
# Date: 2025-06-10

import tensorflow as tf
from PIL import Image
import numpy as np

def load_model():
    # Load a pretrained deep learning model suitable for mobile applications
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    return model

def preprocess_image(image_path):
    # Use Keras API functions to preprocess the image to be classified
    img = tf.keras.utils.load_img(image_path, target_size=(224, 224), color_mode='rgb')
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return np.expand_dims(img_array, axis=0)

def predict_edible(image_path, model):
    # Get set of raw predictions, then determine whether top result is edible
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)[0]
    food_classes = ['apple', 'pizza']
    top_prediction = decoded[0][1] # Get class name for top result
    print(f'This image most likely depicts: {top_prediction}')
    return top_prediction in food_classes

model = load_model()
edible = predict_edible('C:/Users/mailr/code/edible-classifier/test-images/pizza.png', model)
if edible is True:
    print('This represents something edible!')

print("Hello n00bz, we reached the end.")
