import os
import imageio
import skimage
from skimage import color
from skimage.transform import rescale
import numpy as np


def rescale_fourth(image):
    return skimage.transform.rescale(image, .25, anti_aliasing=True, multichannel=True)


def to_gray(image):
    new_img = []
    convert_matrix = np.array([[.299, .587, .114],
                               [-0.14713, -.28886, .436],
                               [.615, -.51499, -.10001]])

    for i in range(len(image)):
        new_row = []
        for j in range(len(image[i])):
            ###### #matix for YUV####

            y1 = convert_matrix.dot(np.vstack(np.array(image[i][j])))[0]

            ### ### # equations for ycbcr ###

            # r=image[i][j][0]
            # g=image[i][j][1]
            # b=image[i][j][2]
            #
            # y2=16+(65.738*r/256)+(129.057*g/256)+(25.064*b/256)
            #
            # print('y1=', y1)
            # print('y2=', y2)
            # print()

            new_row.append(y1)
        new_img.append(new_row)

    return new_img


def to_gray_builtin(image):
    return skimage.color.rgb2gray(image)


def main():
    entries = os.listdir("imagesample")
    try:
        os.mkdir("ShrunkImages")
    except:
        pass

    try:
        os.mkdir("Grayscale")
    except:
        pass

    try:
        os.mkdir("Grayscale_builtin")
    except:
        pass

    for entry in entries:
        old_entry = imageio.imread("imagesample/" + entry)
        new_entry = rescale_fourth(old_entry)
        imageio.imsave("ShrunkImages/" + entry, new_entry)

        new_gray = to_gray(old_entry)
        imageio.imsave("Grayscale/" + entry, new_gray)

        second_gray = to_gray_builtin(old_entry)
        imageio.imsave("Grayscale_builtin/" + entry, second_gray)


main()
