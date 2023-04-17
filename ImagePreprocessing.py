
'''Created on 4/12/23 by Cristian Finley
            last updated: 4/17/23      '''

#############JPEG to RGB Pre-processing#################
from PIL import Image
import numpy as np



'''Turns a JPEG image into a square image and returns RGB matrix of image.
    Variables:
        filename - string - jpeg file name'''
        
def preprocessImage (filename):
    im = Image.open(filename)
    cropped = im.crop((100,100,100,100))
    im = cropped
    im.convert('RGB')
    im_matrix = np.array(im)
    return im_matrix
    
    





#Random PILLOW commands
#im.show()
#print(im.format)
#print(im.mode)
#print(im.size)
#print(im.width, im.height)
#print(im.info)
#left, upper, right, lower
#cropped.show()
#save the cropped image
#cropped.save('images/croppedBeach1.jpg')