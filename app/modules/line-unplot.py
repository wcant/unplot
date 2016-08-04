
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby
from operator import itemgetter


def histogram_plot(data):

    plt.hist(data, bins=10, normed=False)
    plt.show()


def most_common(data):

    SL = sorted((x, i) for i, x in enumerate(data))
    groups = groupby(SL, key=itemgetter(0))

    # function is used as key in max()
    # counts the number of occurrences of the enumerated data
    # max() will then return the data value with the highest count
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(data)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)

        return count, -min_index

    return max(groups, key=_auxfun)[0]


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

    print(most_common(flatarray))


if __name__ == "__main__":

    main()
