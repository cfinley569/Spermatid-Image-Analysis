# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:59:46 2023

@author: Cristian Finley
"""


'''Created on 4/17/23 by Cristian Finley
            last updated: 4/17/23 
functions for adding, deleting, and managing training data for model'''

from ImagePreprocessing import preprocessImage
import numpy as np


'''takes in a filename and adds the file to the training data set.  
Adds data to three seperate files, image array to TrainingDataX, correct
step value to TrainingDataY, and filename to trainingfilenames.txt
returns void'''
def addData (filename):
    y_train = np.loadtxt("TrainingDataY")
    step = filename[-6:-4] 
    y_train = np.append(y_train,int(step))
    np.savetxt("TrainingDataY", y_train)
    
    x_train = np.loadtxt("TrainingDataX")
    im_matrix = preprocessImage(filename)
    x_train = np.append(x_train,im_matrix)
    np.savetxt("TrainingDataX", x_train)
    
    trainingdata = open('trainingfilenames.txt','a')
    trainingdata.writelines(filename+'\n')
    trainingdata.close()

'''deletes all stored images and training data
returns void'''
def deleteAllData():
    data = open('TrainingDataX','w')
    data.close()
    data = open('TrainingDataY', 'w')
    data.close()
    data = open('trainingfilenames.txt','w')
    data.close()


'''Uses a filename to find the storage index of that image and then removes 
the image from the x and y training files
returns void
    - may work really slowly
    - optimizie (use linked list?!?!)'''
def deleteSelectData (filename):
    
    #find the index of the filename
    data = open('TrainingDataX','r')
    filenames = data.readlines()
    for x,i in enumerate(filenames):
        if i == filename: 
            index = x
    filenames.pop(x)
    data.close()
    
    #clear filenames and write without removed file
    data = open('TrainingDataX','w')
    data.write(filenames)
    data.close()
    
    #remove x component
    data = np.loadtxt('TrainingDataX')
    data.pop(index)
    np.savetxt('TrainingDataX',data)
    
    #remove y component
    data = np.loadtxt('TrainingDataY')
    data.pop(index)
    np.savetxt('TrainingDataY',data)
    data = np.load
    
'''Loads the training data from saved files in the form of a tuple
returns tuple (x_train,y_train)
x_train is array of image arrays to be fed into model
y_train is array of correct step values to check model against'''
def loadDataSet ():
    x_train = np.loadtxt("TrainingDataX")
    y_train = np.loadtxt("TrainingDataY")
    return x_train,y_train













