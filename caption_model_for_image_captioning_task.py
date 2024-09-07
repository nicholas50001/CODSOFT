import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Add

def build_model(vocab_size, max_length):
    inputs1 = Input(shape=(2048,))
    features1 = Dense(256, activation='relu')(inputs1)

    inputs2 = Input(shape=(max_length,))
    embedding = Embedding(vocab_size, 256)(inputs2)
    lstm = LSTM(256)(embedding)

    combined = Add()([features1, lstm])
    outputs = Dense(vocab_size, activation='softmax')(combined)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model
