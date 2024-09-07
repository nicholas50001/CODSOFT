import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from feature_extraction import extract_features

model = load_model('../models/image_captioning_model.h5')
with open('../data/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

max_length = 34  

def generate_caption(model, tokenizer, photo, max_length):
    in
