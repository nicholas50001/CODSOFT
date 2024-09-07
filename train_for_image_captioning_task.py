import numpy as np
import pickle
from tensorflow.keras.utils import to_categorical
from caption_model import build_model

with open('../data/features.pkl', 'rb') as f:
    features_dict = pickle.load(f)
with open('../data/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)
sequences = np.load('../data/sequences.npy')

vocab_size = len(tokenizer.word_index) + 1
max_length = sequences.shape[1]

X1, X2, y = [], [], []
for img_name, seq in zip(image_names, sequences):
    for i in range(1, len(seq)):
        X1.append(features_dict[img_name])
        X2.append(seq[:i])
        y.append(to_categorical(seq[i], num_classes=vocab_size))

X1, X2, y = np.array(X1), pad_sequences(X2, maxlen=max_length), np.array(y)

model = build_model(vocab_size, max_length)

model.fit([X1, X2], y, epochs=20, batch_size=64, verbose=1)

model.save('../models/image_captioning_model.h5')
