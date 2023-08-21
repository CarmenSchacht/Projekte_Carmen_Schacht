import docx
import glob
#import xlsxwriter

class Wort:
    def __init__(self, realisierung, wortIndex):
        self.realisierung=realisierung
        self.wortIndex=wortIndex


class Ausserung:
    def __init__(self, aNummer, aInhalt):
        self.aNummer=aNummer
        self.aInhalt=aInhalt
        self.woerter=[]
        self.fuellWoerter()

    def fuellWoerter(self):
        zeichenBlacklist=['.', ',', '(', ')', '[', ']', '/', ';', ':', '-', '…']
        for badChar in zeichenBlacklist:
            self.aInhalt=self.aInhalt.replace(badChar, '')
        self.aInhalt=self.aInhalt.lower()
        alleWoerter=self.aInhalt.split()
        aktuellerWortIndex=1
        for aktuellesWort in alleWoerter:
            self.woerter.append(Wort(aktuellesWort, aktuellerWortIndex))
            aktuellerWortIndex+=1


class Stimulus:
    def __init__(self, sName, stimulusDaten):
        self.sName=sName
        self.beschreibung=[]
        self.stimulusDaten=stimulusDaten
        self.fuellBeschreibung()

    def fuellBeschreibung(self):
        for aktuelleAusserung in self.stimulusDaten:
            aktuelleAusserungsnummer=int(aktuelleAusserung[0:2])
            aktuellerAusserunginhalt=aktuelleAusserung[3:]
            self.beschreibung.append(Ausserung(aktuelleAusserungsnummer, aktuellerAusserunginhalt))



class Proband:
    def __init__(self, dateiname):
        self.dateiname=dateiname
        self.datei = self.leseTranskript(docx.Document(dateiname))
        self.stimuli=[]
        self.pNummer=self.datei[0]
        self.gender=self.datei[1]
        self.profession=self.datei[2]
        self.bilingualitaet=self.datei[3]
        self.fuellStimuli()

    def leseTranskript(self, transkript):
        extrahiert=[]
        for p in transkript.paragraphs:
            extrahiert.append(p.text)
        return extrahiert

    def fuellStimuli(self):
        for x in range(5):
            zeilenIndex = self.datei.index('Built-B' + str(x + 1))
            zeilenIndex = zeilenIndex + 2
            aktuellerBildName='B'+str(x+1)
            aktuelleAusserungen=[]
            while not "<" in self.datei[zeilenIndex]:
                aktuelleZeile = self.datei[zeilenIndex]
                aktuelleAusserungen.append(aktuelleZeile)
                zeilenIndex += 1
            self.stimuli.append(Stimulus(aktuellerBildName, aktuelleAusserungen))



def findeWort(probNummer, wort, gender, profession, bild, languageStatus, badWordsInc, probanden):
    wortliste=[]
    for proband in probanden:
        if proband.pNummer==probNummer or probNummer is None:
            if proband.gender==gender or gender is None:
                if proband.profession==profession or profession is None:
                    if proband.bilingualitaet==languageStatus or languageStatus is None:
                        for stimulus in proband.stimuli:
                            if stimulus.sName==bild or bild is None:
                                for ausserung in stimulus.beschreibung:
                                    for begriff in ausserung.woerter:
                                        if begriff.realisierung == wort:
                                            wortliste.append(wort)
                                        elif wort is None:
                                            wortliste.append(begriff.realisierung)

    f=open(str(probNummer)+'_'+str(wort)+'_'+str(gender)+'_'+str(profession)+'_'+str(bild)+'_'+str(languageStatus)+'_'+str(badWordsInc)+'.csv', 'w')
    print('WORT  |  ANZAHL')
    f.write('Wort;Anzahl\n')

    gefundeneWoerter=[]
    stopwordListe = ['der', 'die', 'das']
    for ausdruck in wortliste:
        if ausdruck not in gefundeneWoerter:
            gefundeneWoerter.append(ausdruck)
            if ausdruck in stopwordListe and badWordsInc:
                print(ausdruck + ' | ' + str(wortliste.count(ausdruck)))
                f.write(ausdruck+';'+str(wortliste.count(ausdruck))+'\n')

            elif ausdruck not in stopwordListe:
                print(ausdruck + ' | ' + str(wortliste.count(ausdruck)))
                f.write(ausdruck + ';' + str(wortliste.count(ausdruck)) + '\n')

    f.close()


files=glob.glob('./*.docx')
probanden=[]
for probandenDatei in files:
    probanden.append(Proband(probandenDatei))


findeWort(None, None, None, 'L', None, None, True, probanden)

# print(probanden[1].stimuli[0].beschreibung[0].woerter[2].realisierung)



