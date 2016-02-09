import csv
"""
Ein Program zum einlesen von CSV Dateien (mit unterschiedlichen Dialekt)
und das ausgeben davon.
"""
__author__ = "Mateusz Gala"
__version__ = "1.0"

class csv1:
    # Oeffnen der beiden Dateien.
    @staticmethod
    def openfile(name, like):
        return open(name, like)

    # Der Dialekt wird mittels eines Sniffers geholt
    @staticmethod
    def dialekt(f):
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        return dialect

    @staticmethod
    def set_delimiter(name,delimiter):
        return csv.register_dialect(name, delimiter)

    # Das File wird ausgelesen mit dem erfassten Dialekt.
    @staticmethod
    def read(f, dialect):
        r = csv.reader(f, dialect)
        return r

    #die files werden in 1 file umgewandelt
    @staticmethod
    def mergefiles(r1,r2):
        output = []
        for row in r1:
            output.append(row)
        for row in r2:
            output.append(row)
        return output

    #ein outputfile wird erstellt
    #in das neue file wird mit einem beliebigen dialekt geschrieben
    @staticmethod
    def outputfile(outputfilename, dialekt, output):
        writer = csv.writer(outputfilename, dialekt)
        for all in output:
            writer.writerow(all)
        return writer
    @staticmethod
    def close_file(file):
        file.close()