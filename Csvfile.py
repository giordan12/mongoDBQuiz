import csv


def importFile(filename):
    file = open(filename, 'rb')
    reader = csv.DictReader(file)
    return reader
