# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:59:46 2023

@author: Cristian Finley
"""


'''Created on 4/17/23 by Cristian Finley
            last updated: 4/17/23 
functions for adding, deleting, and managing training data for model'''

from ImagePreprocessing import preprocessImage


def addData (filename):
    trainingdata = open('TrainingData.py', 'a')   
    im_matrix = preprocessImage(filename)
    
    meta = trainingdata.readline()
    numimages = meta[0] + 1
    trainingdata.writelines(numimages+meta[1:])[0]
    
    
    trainingdata.write(im_matrix + '\n')
    trainingdata.close()
    
    #TODO : add functionality for adding data to training set
    pass



def deleteData ():
    #TODO : add functionality for deleting data from training set
    pass
















