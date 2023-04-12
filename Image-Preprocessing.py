
'''Created on 4/12/23 by Cristian Finley
            last updated: 4/12/23      '''

#############JPEG to RGB Pre-processing#################


from PIL import Image

im = Image.open("Image.jpg")
im.show()
im = im.rotate(45)
im.show()






