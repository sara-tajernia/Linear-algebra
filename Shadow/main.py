import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image

def get_pic():     #geting the relative or absolute path of picture
    user = input('Enter directory: ')
    pic_data = image.imread(user)
    return pic_data

def shade_pic(pic):     #find the shade of pic in white and gray by mutiply matrix ([1 0][0.05 1] to each point
    shade = np.full((pic.shape[0], int(1.05*pic.shape[1]), 3), 255 , dtype= 'uint8')
    for i in range (pic.shape[0]):
        for j in range (pic.shape[1]):
            if np.any(pic[i][j]< 230):
                shade[i][int((0.05 * i) + j)] = [140, 130, 130]
    return shade

def colorful_pic(pic, shade):      #set the color point of first pic in the in the right location of shade pic
    size = pic.shape
    for i in range(size[0]):
        for j in range(size[1]):
            if np.any(pic[i][j]< 230):
                shade[i][j]= pic[i][j]
    return shade

if __name__ == '__main__':
    pic = get_pic()
    shade = shade_pic(pic)
    final = colorful_pic(pic, shade)
    plt.imshow(final)
    plt.show()