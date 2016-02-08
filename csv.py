import csv
"""
Ein Program zum einlesen von CSV Dateien (mit unterschiedlichen Dialekt)
und das ausgeben davon.
"""
__author__ = "Mateusz Gala"
__version__ = "1.0"


output = []
# Oeffnen der beiden Dateien.
with open('Book1.csv') as f:
    with open('Book2.csv') as g:

        # Der Dialekt wird mittels eines Sniffers geholt
        dialect = csv.Sniffer().sniff(f.read(1024))
        dialect2 = csv.Sniffer().sniff(g.read(1024))

        # Eine seek methode.
        f.seek(0)
        g.seek(0)
        # Das File wird ausgelesen mit dem erfassten Dialekt.
        r = csv.reader(f, dialect)
        r2 = csv.reader(g, dialect2)

        #ein outputfile wird erstellt
        outputfile = open('output.csv', "wt")
        #in das neue file wird mit dem dialekt = ; geschrieben
        csv.register_dialect('semicolon', delimiter=';')
        writer = csv.writer(outputfile, dialect='semicolon')

        #auslesen der Dateinen + ausgeben von output.csv im gleichen Ordner
        for row in r:
            output.append(row)
        for row in r2:
            output.append(row)
        for all in output:
            writer.writerow(all)