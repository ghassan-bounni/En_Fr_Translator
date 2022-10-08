import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import re
# import tensorflow as tf
from keras.models import load_model
import logging
import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class En_Fr_Translator:

    def __init__(self, model_path):
        logging.info("En_Fr_Translator class initialized")
        self.model = load_model(model_path)
        self.df = pd.read_csv('model/text.csv')
        self.eng_tokenizer = self.create_tokenizer(self.df.English)
        self.fr_tokenizer = self.create_tokenizer(self.df.French)
        logging.info("Model is loaded!")

    def predict(self, en_text):
        # preprocessing the input
        text = ' '.join(re.sub(r'[^\w\s]', '', en_text).split())
        text = self.eng_tokenizer.texts_to_sequences([text])
        text = pad_sequences(text, 15, padding='post')
        # getting the prediction vectors
        prediction = self.model.predict(text)[0]
        # getting the index of each word in the vectors
        indices = np.argmax(prediction, axis=-1)
        # getting the respective word from the tokenizer
        return ' '.join([self.fr_tokenizer.index_word[index] for index in indices if index != 0])

    def create_tokenizer(self, lines):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(lines)
        return tokenizer
