from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.callbacks import EarlyStopping
from keras.layers import Dropout
import keras
import os
import pandas as pd
import numpy as np

# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 10000
# Max number of words in each sentence.
MAX_SEQUENCE_LENGTH = 250
# This is fixed.
EMBEDDING_DIM = 100
#model = load_model('guj_without_stop_words.h5')
#model = load_model('guj_with_stop_words.h5')
#print("done")
#new_sent = input("Enter a sentence to predict it's emotion: ")
import pickle
with open("models/token", 'rb') as f:
    tokenizer = pickle.load(f)


def predicted(new_sent):    
    new_sent = new_sent
    for i in new_sent:
        new_sent = [i]
        
        model = load_model('models/new_duo.h5')
        
        #tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
        #tokenizer.fit_on_texts(new_sent)
        #word_index = tokenizer.word_index
        #print('Found %s unique tokens.' % len(word_index))
        
        seq = tokenizer.texts_to_sequences(new_sent)
        #print(seq)
        padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
        #print(padded)
        pred = model.predict(padded)
        labels = ['neg', 'pos'] # [0,1]
        #print(new_sent," : ", labels[np.argmax(pred)])
        #model.summary()
        del model
        if (labels[np.argmax(pred)] == 'neg'):
            model = load_model('models/negative_guj.h5')
            pred = model.predict(padded)
            labels = ['anger', 'fear', 'sad']
        else:
            model = load_model('models/positive_guj.h5')
            pred = model.predict(padded)
            labels = ['joy', 'surprise', 'love'] 
        del model
        print(new_sent,"   ",labels[np.argmax(pred)])
    return labels[np.argmax(pred)]   
    
'''   
lt = ['મને લાગણી છે કે તે ખુશ અને આનંદિત હતી' ,
      'હું રોમેન્ટિક પણ અનુભવું છું',
      'હું તદ્દન નર્વસ અનુભવતો હતો',
      'હું હજી પણ એટલી ઉશ્કેરાયેલી અનુભવું છું',
      'હું ક્યારેક બધા રમુજી લાગે']
x = predicted(lt)
#print(x)'''

