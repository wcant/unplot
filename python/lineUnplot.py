from numpy import *
from PIL import Image

class lineUnplot():

    def __init__(self):
        self.image = None

    def getRgbArray (self):
        im = Image.open(self.image)
