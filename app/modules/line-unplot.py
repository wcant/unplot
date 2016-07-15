
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def histogram_plot(data):

    plt.hist(data, bins=10, normed=False)
    plt.show()

def main():

    testimg = "../../uploads/untitled.jpg"
    rgbarray = None
    with Image.open(testimg) as im:
        rgbarray = np.array(im)

    print("Array shape is : %s" % str(rgbarray.shape))

    bitarray = np.asarray(rgbarray, dtype='uint32')
    bitarray = ((bitarray[:, :, 0] << 16) + (bitarray[:, :, 1] << 8) + bitarray[:, :, 2])

    flatarray = bitarray.flatten()
    hexarray = [hex(i) for i in flatarray]
    
    histogram_plot(flatarray)


if __name__ == "__main__":

    main()
