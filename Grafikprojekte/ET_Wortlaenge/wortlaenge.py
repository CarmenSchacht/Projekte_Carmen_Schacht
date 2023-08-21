import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

v = np.array([1, 2])
plus = np.array([2, 2])
fontsFolder = 'C:\Windows\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.ttf'), 150)
words = ['Nest', 'Besen', 'Kuh', 'Elefant', 'Boot', 'Flugzeug', 'Cent', 'Flasche', 'Topf', 'Fernseher', 'Mund', 'Globus', 'Ente', 'Pinguin', 'Maus', 'Schlange', 'Stift', 'Tasche', 'Korn', 'Apfel', 'Tür', 'Hubschrauber', 'Fuß', 'Auge', 'Hai', 'Katze', 'Huhn', 'Finger', 'Schiff', 'Fahrrad', 'Ball', 'Zitrone', 'Brot', 'Erdbeere', 'Ei', 'Kirsche', 'Zug', 'Ziege', 'Baum', 'Hummel', 'Haus', 'Löffel', 'Hose', 'Banane']
for i in range(22):
    if i > 0:
        v = v+plus
    image1 = Image.open(str(v[0]) + '.png')
    widthcrop, heightcrop = image1.size
    image1square = image1.crop((widthcrop*0.15, 0, widthcrop*0.85, heightcrop))
    stimwidth, stimheight = image1square.size
    draw1 = ImageDraw.Draw(image1square)
    stim1 = draw1.text((stimwidth*0.4, stimheight*0.9), str(words[v[0]-1]), fill='black', font=arialFont)
    image2 = Image.open(str(v[1]) + '.png')
    image2square = image2.crop((widthcrop*0.15, 0, widthcrop*0.85, heightcrop))
    draw2 = ImageDraw.Draw(image2square)
    stim2 = draw2.text((stimwidth * 0.4, stimheight * 0.9), str(words[v[1]-1]), fill='black', font=arialFont)
    width, height = image1square.size
    hg = Image.new('RGBA', (width*2, height), 'white')
    coord1 = [0, 0]
    coord2 = [width+1, 0]

    for j in range(2):
        if j == 0:
            a_1 = [coord1, coord2]
            A = np.array(a_1)
        elif j == 1:
            a_1 = [coord2, coord1]
            A = np.array(a_1)
        hgKopie = hg.copy()
        paste1 = [int(coord) for coord in A[0]]
        paste2 = [int(coord) for coord in A[1]]
        hgKopie.paste(image1square, tuple(paste1))
        hgKopie.paste(image2square, tuple(paste2))
        hgKopie.save('Stimulus' + str(words[v[1]-1]) + '_' + str(words[v[0]-1]) + '.png')
        hgKopie = hg.copy()
        hgKopie.paste(image1square, tuple(paste2))
        hgKopie.paste(image2square, tuple(paste1))
        hgKopie.save('Stimulus' + str(words[v[0]-1]) + '_' + str(words[v[1]-1]) + '.png')
