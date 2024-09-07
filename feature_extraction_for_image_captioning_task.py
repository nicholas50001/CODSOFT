import os
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import pickle

model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features

image_folder = '../data/images/'
features_dict = {}
for img_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_name)
    features = extract_features(img_path, model)
    features_dict[img_name] = features

with open('../data/features.pkl', 'wb') as f:
    pickle.dump(features_dict, f)
