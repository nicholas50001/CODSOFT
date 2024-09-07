import os
import numpy as np
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('../data/captions.json', 'r') as f:
    captions_dict = json.load(f)

captions = []
image_names = []
for img_name, caption_list in captions_dict.items():
    for caption in caption_list:
        captions.append(caption)
        image_names.append(img_name)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(captions)
sequences = tokenizer.texts_to_sequences(captions)

word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

max_length = max(len(seq) for seq in sequences)
sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

with open('../data/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
np.save('../data/sequences.npy', sequences)
