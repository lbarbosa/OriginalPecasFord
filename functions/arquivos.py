'''
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
'''
import chardet


def openFile(filename, Encoding):
    fileline = []
    with open(filename, "r", encoding=Encoding) as fileLines:
        for line in fileLines:
            fileline.append(line.strip())
    return fileline


def proc_Line(fileLines):
    for line in fileLines:
        if line in "LOCK TABLES `cad_produtos` WRITE;":
       # line = line.strip()
            print(line)

#   return fileline

def returnEncoding(fileLines):
    print("returnEncoding")
    encoding = chardet.detect(open(fileLines, 'rb').read())['encoding']
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
