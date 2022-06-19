# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""
import chardet


# Open the file and create a Python list
def openFile(filename, Encoding):
    fileline = []
    with open(filename, "r", encoding=Encoding) as fileLines:
        for line in fileLines:
            fileline.append(line.strip())

    fileLines.close()
    return fileline


# Process the original file to find the start line and end line of products
def proc_Line(fileLines):
    count_begin = 0
    count_end = 0
    count = 0

    for line in fileLines:
        count = count + 1
        if line in "LOCK TABLES `cad_produtos` WRITE;":
            if line != "":
                count_begin = count
                print(count_begin)
            else:
                count_begin = 0
        else:
            count_begin = 0
        if line in "DROP TABLE" + " IF EXISTS `cad_produtos_fornecedores`;":
            if line != "":
                count_end = count
                count_end = count_end - 3
                print(count_end)
            else:
                count_begin = 0
        else:
            count_end = 0
    return count_begin, count_end


# valid file encoding type
def returnEncoding(fileLines, encoding):
    print("returnEncoding")
    if encoding != "":
        encoding = encoding
    else:
        encoding = chardet.detect(open(fileLines, 'rb').read())['encoding']

    print(encoding)
    return encoding


class file:

    def __init__(self, fileName, extension, encoding, openType):
        self.fileName = fileName
        self.extension = extension
        self.encoding = encoding
        self.openType = openType

    def setFineName(self, filename):
        self.fileName = filename

    def setExtension(self, extension):
        self.extension = extension

    def getFineName(self, filename):
        return self.fileName

    def getExtension(self, extension):
        return self.extension

    def setEncoding(self, encoding):
        self.encoding = encoding

    def setOpenType(self, openType):
        self.extension = openType

    def getEncoding(self, encoding):
        return self.encoding

    def getOpenType(self, openType):
        return self.openType
