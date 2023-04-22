# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:07:59 2023

@author: Cristian Finley
"""

from ImagePreprocessing import *
from DataManager import *
import tensorflow as tf
import os
import tkinter as tk


def main ():
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    entry = tk.Entry()
    greeting.pack()
    entry.pack()
    window.mainloop()
    while entry.get()[-1] != '\n':
        continue
    print(entry.get())
    print("test")



'''creates a new sequential neural network
    inputs:  none
    returns:
        model - TensorFlow sequential model'''
def createModel():
    #TODO : add ability to control creation of layers and model more easily
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
        ])
    return model

'''loads a saved model from the file "savedModel.txt" and returns the read model'''
def loadModel():
    savefile = open('savedModel.txt','r')
    model = savefile.read()
    savefile.close()
    return model

'''Saves the inputted model into the file "saveModel.txt", overwriting anything already there'''
def saveModel(model):
    #TODO : add functionality for not overwriting file and adding in version number or something
    model.save('C:/Users/Cristian Finley/Documents/GitHub/Spermatid-Image-Analysis/savedModel')
    return
    
    
'''Trains a model by taking in a set of inputs and trying to make the outputs of the model match inputted correct outputs'''
def train(model):
    #TODO: add functionality for inputting training data and training data correct answers
    print("TensorFlow version:", tf.__version__)
    trainingData,trainingDataSteps = loadDataSet()
    
    predictions = model(trainingData[:1]).numpy()
    predictions
    tf.nn.softmax(predictions).numpy()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(trainingDataSteps, predictions).numpy()
    model.compile(optimizer='adam',loss = loss_fn,metrics =['accuracy'])
    
    
    model.fit(trainingData,trainingDataSteps, y_train, epochs=4)
    model.evaluate(x_test,y_test,verbose=2)
    
    probability_model = tf.keras.Sequential([
      model,
      tf.keras.layers.Softmax()
    ])
    
    probability_model(x_test[:5])


'''Used to test the accuracy of the model without training'''
def test(model):
    # TODO: add input functionality for test data to test on
    model.evaluate(x_test,y_test,verbose=2)
    
    probability_model = tf.keras.Sequential([
      model,
      tf.keras.layers.Softmax()
    ])
    
    probability_model(x_test[:5])



main()



######### code used to save a model in the middle of training ############
# checkpoint_path = 'savedModel/cp.ckpt'
# checkpoint_dir = os.path.dirname(checkpoint_path)
# cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,
#                                              verbose=1)
# print(cp_callback)