import docx
import glob


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

    def getWoerter(self):
        ausserungString=''
        for wort in self.woerter:
            ausserungString+=wort.realisierung+' '
        return ausserungString[:-1]

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


def findeWort(probNummer, wort, folgeWort, gender, profession, bild, languageStatus, badWordsInc, probanden):
    f = open(
        str(probNummer) + '_' + str(wort) + '_' + str(folgeWort) + '_' + str(gender) + '_' + str(profession) + '_' + str(bild) + '_' + str(
            languageStatus) + '_' + str(badWordsInc) + '.csv', 'w')
    f.write('Wort;Aussage;ProbNr;Stimulus;AussagenNr;LanguageStatus;Profession;Gender\n')
    for proband in probanden:
        if proband.pNummer==probNummer or probNummer is None:
            if proband.gender==gender or gender is None:
                if proband.profession==profession or profession is None:
                    if proband.bilingualitaet==languageStatus or languageStatus is None:
                        for stimulus in proband.stimuli:
                            if stimulus.sName==bild or bild is None:
                                for ausserung in stimulus.beschreibung:
                                    for begriff in ausserung.woerter:
                                        if begriff.realisierung == wort and begriff.wortIndex < len(ausserung.woerter) and ausserung.woerter[begriff.wortIndex].realisierung == folgeWort:
                                            f.write(begriff.realisierung + ' ' + folgeWort + ';')
                                            f.write(ausserung.getWoerter() + ';')
                                            f.write(proband.pNummer + ';')
                                            f.write(stimulus.sName + ';')
                                            f.write(str(ausserung.aNummer) + ';')
                                            f.write(proband.bilingualitaet + ';')
                                            f.write(proband.profession + ';')
                                            f.write(proband.gender +'\n')
                                        elif begriff.realisierung == wort and folgeWort is None:
                                            f.write(begriff.realisierung + ';')
                                            f.write(ausserung.getWoerter() + ';')
                                            f.write(proband.pNummer + ';')
                                            f.write(stimulus.sName + ';')
                                            f.write(str(ausserung.aNummer) + ';')
                                            f.write(proband.bilingualitaet + ';')
                                            f.write(proband.profession + ';')
                                            f.write(proband.gender + '\n')

    f.close()


files=glob.glob('./*.docx')
probanden=[]
for probandenDatei in files:
    probanden.append(Proband(probandenDatei))


findeWort(None, 'man', None, None, None, None, None, True, probanden)
