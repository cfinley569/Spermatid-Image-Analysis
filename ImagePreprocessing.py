
'''Created on 4/12/23 by Cristian Finley
            last updated: 4/17/23      '''

#############JPEG to RGB Pre-processing#################
from PIL import Image
import numpy as np

'''Turns a JPEG image into an image with width = 400 px and height = 400 px unless otherwise specified
inputs: 
    filename - image file compatible with pillo
    width(optional) - desired image array width
    height(optional) - desired image array height
returns:
    matrix of RGB px values'''
def preprocessImage (filename,width=400,height=400):
    im = Image.open(filename)
    width = 400
    height = 400
    
    if im.size[0] > width:
        im = im.crop((((im.size[0]-width)/2),0,(im.size[0]-(im.size[0]-width)/2),im.size[1]))
    if im.size[1] > height:
        im = im.crop((0,((im.size[1]-height)/2),im.size[0],(im.size[1]-(im.size[1]-height)/2)))
    im_matrix = np.array(im)
    print(im_matrix.size)
    im.close()
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