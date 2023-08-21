#import PIL
#from PIL import Image
#import os
#import numpy as np

#dateisystem = os.listdir(C:\Users\Carmen\Desktop\Arbeitsfläche\MA EMF\Praktikum und Hiwi\ET_Katrin_Jenny)

#for i in dateisystem:
  #  bildpaare = os.listdir(dateisystem[i])

#image1 = Image.open('1.jpg')
##image2 = Image.open('2.jpg')
#image3 = Image.open('3.jpg')
#image4 = Image.open('4.jpg')
#hg = Image.open('Hintergrund.jpg')
#numbers = Image.open('numbers.png')
#width, height = hg.size
#coord1 = (0, 0)
#coord2 = (width/2, 0)
#coord3 = (0, height/2)
#coord4 = (width/2, height/2)
#for j in range(4):
#    a_1 = [(0, 0), (width/2, 0), (0, height/2), (width/2, height/2)]
#    A = np.array(a_1)
#    if j == 1:
#        A[0], A[1] = A[1], A[0]
#        A[2], A[3] = A[3], A[2]
#    if j == 2:
#        A[0], A[2] = A[2], A[0]
#        A[1], A[3] = A[3], A[1]
#    if j == 3:
#        A[0], A[1] = A[1], A[0]
#        A[2], A[3] = A[3], A[2]
#        A[0], A[2] = A[2], A[0]
#        A[1], A[3] = A[3], A[1]
#    for n in range(6):
#        hgKopie = hg.copy()
#        paste1 = A[0]
#        paste2 = A[1]
#        paste3 = A[2]
#        paste4 = A[3]
#        hgKopie.paste(image1, A[0])
#        hgKopie.paste(image2, A[1])
#        hgKopie.paste(image3, A[2])
#        hgKopie.paste(image4, A[3])
#        hgKopie.save('Stimulus1' + str(j) + '_' + str(n) + '.png')
#        hgKopie.paste(numbers, (0, 0))
#        hgKopie.save('Stimulus1_Zahlen' + str(j) + '_' + str(n) + '.png')
#        if n == 0:
#            A[2], A[3] = A[3], A[2]
#        if n == 1:
#            A[1], A[3] = A[3], A[1]
#        if n == 2:
#            A[2], A[3] = A[3], A[2]
#        if n == 3:
#            A[1], A[3] = A[3], A[1]
#        if n == 4:
#            A[2], A[3] = A[3], A[2]
#coord1 = [0, 0]
#coord2 = [width // 2, 0]
#coord3 = [0, height // 2]
#coord4 = [width // 2, height // 2]

import numpy as np
from PIL import Image

v = np.array([1, 2, 3, 4])
plus = np.array([4, 4, 4, 4])
for i in range(16):
    if i > 0:
        v = v+plus
    image1 = Image.open(str(v[0]) + '.png')
    image2 = Image.open(str(v[1]) + '.png')
    image3 = Image.open(str(v[2]) + '.png')
    image4 = Image.open(str(v[3]) + '.png')
    hg = Image.open('Hintergrund.png')
    numbers = Image.open('raster_zahlen.png')
    raster = Image.open('raster.png')
    width, height = hg.size
    coord1 = [584, 413]
    coord2 = [5431, 413]
    coord3 = [584, 3547]
    coord4 = [5431, 3547]

    for j in range(24):
        if j == 0:
            a_1 = [coord1, coord2,
                   coord3, coord4]
            A = np.array(a_1)
        elif j == 1:
            a_1 = [coord1, coord2,
                   coord4, coord3]
            A = np.array(a_1)
        elif j == 2:
            a_1 = [coord1, coord3,
                   coord4, coord2]
            A = np.array(a_1)
        elif j == 3:
            a_1 = [coord1, coord3,
                   coord2, coord4]
            A = np.array(a_1)
        elif j == 4:
            a_1 = [coord1, coord4,
                   coord2, coord3]
            A = np.array(a_1)
        elif j == 5:
            a_1 = [coord1, coord4,
                   coord3, coord2]
            A = np.array(a_1)
        elif j == 6:
            a_1 = [coord2, coord1,
                   coord3, coord4]
            A = np.array(a_1)
        elif j == 7:
            a_1 = [coord2, coord1,
                   coord4, coord3]
            A = np.array(a_1)
        elif j == 8:
            a_1 = [coord2, coord3,
                   coord4, coord1]
            A = np.array(a_1)
        elif j == 9:
            a_1 = [coord2, coord3,
                   coord1, coord4]
            A = np.array(a_1)
        elif j == 10:
            a_1 = [coord2, coord4,
                   coord1, coord3]
            A = np.array(a_1)
        elif j == 11:
            a_1 = [coord2, coord4,
                   coord3, coord1]
            A = np.array(a_1)
        elif j == 12:
            a_1 = [coord3, coord2,
                   coord1, coord4]
            A = np.array(a_1)
        elif j == 13:
            a_1 = [coord3, coord2,
                   coord4, coord1]
            A = np.array(a_1)
        elif j == 14:
            a_1 = [coord3, coord1,
                   coord4, coord2]
            A = np.array(a_1)
        elif j == 15:
            a_1 = [coord3, coord1,
                   coord2, coord4]
            A = np.array(a_1)
        elif j == 16:
            a_1 = [coord3, coord4,
                   coord2, coord1]
            A = np.array(a_1)
        elif j == 17:
            a_1 = [coord3, coord4,
                   coord1, coord2]
            A = np.array(a_1)
        elif j == 18:
            a_1 = [coord4, coord2,
                   coord3, coord1]
            A = np.array(a_1)
        elif j == 19:
            a_1 = [coord4, coord2,
                   coord1, coord3]
            A = np.array(a_1)
        elif j == 20:
            a_1 = [coord4, coord3,
                   coord1, coord2]
            A = np.array(a_1)
        elif j == 21:
            a_1 = [coord4, coord3,
                   coord2, coord1]
            A = np.array(a_1)
        elif j == 22:
            a_1 = [coord4, coord1,
                   coord2, coord3]
            A = np.array(a_1)
        elif j == 23:
            a_1 = [coord4, coord1,
                   coord3, coord2]
            A = np.array(a_1)
        hgKopie = hg.copy()
        paste1 = [int(coord) for coord in A[0]]
        paste2 = [int(coord) for coord in A[1]]
        paste3 = [int(coord) for coord in A[2]]
        paste4 = [int(coord) for coord in A[3]]
        hgKopie.paste(image1, tuple(paste1))
        hgKopie.paste(image2, tuple(paste2))
        hgKopie.paste(image3, tuple(paste3))
        hgKopie.paste(image4, tuple(paste4))
        hgKopie.paste(raster, raster)
        hgKopie.save('Stimulus' + str(i+1) + '_' + str(j+1) + '.png')
        hgKopie = hg.copy()
        hgKopie.paste(image1, tuple(paste1))
        hgKopie.paste(image2, tuple(paste2))
        hgKopie.paste(image3, tuple(paste3))
        hgKopie.paste(image4, tuple(paste4))
        hgKopie.paste(numbers, numbers)
        hgKopie.save('Stimulus' + str(i+1) + '_Zahlen' + str(j+1) + '.png')

