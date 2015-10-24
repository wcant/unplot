import os.path
from numpy import *
from PIL import Image

class lineUnplot():

    def __init__(self, img=''):
        self.img = img

    def getRgbArray (self):
        img = Image.open(self.img)
	self.imgFormat = img.format
	self.imgSize = img.size


#pass in file location to class
l = lineUnplot("../uploads/untitled.jpg")
