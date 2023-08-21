import PIL

for x in range(60):
    for y in range(12):
        from PIL import Image
        ziffernblatt = Image.open('Ziffernblatt.png')
        minutenzeiger = Image.open('Minutenzeiger.png')
        stundenzeiger = Image.open('Stundenzeiger.png')
        ziffernblattKopie = ziffernblatt.copy()
        minutenRotiert = minutenzeiger.rotate(x*-6)
        stundenRotiert = stundenzeiger.rotate(y*-30-0.5*x)
        ziffernblattKopie.paste(minutenRotiert, minutenRotiert)
        ziffernblattKopie.paste(stundenRotiert, stundenRotiert)
        ziffernblattKopie.save(str(y) + '.' + str(x) + 'Uhr.png')
