# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""
import chardet


# valid file encoding type
def returnEncoding(fileLines, encoding):
    #print("returnEncoding")
    if encoding != "":
        encoding = encoding
    else:
        encoding = chardet.detect(open(fileLines, 'rb').read())['encoding']
    return encoding


# Open the file and create a Python list
def openFileSql(filename, Encoding):
    #print("openFileSql")
    fileline = []
    with open(filename, "r", encoding=Encoding) as fileLines:
        for line in fileLines:
            fileline.append(line.strip())
    fileLines.close()
    return fileline


# Process the original file to find the start line and end line of products
def procLineSql(fileLines):
    #print("proc_Line")
    count_begin = 0
    count_end = 0
    count = 0

    for line in fileLines:
        count = count + 1
        if line in "LOCK TABLES `cad_produtos` WRITE;":
            if line != "":
                count_begin = count

        if line in "DROP TABLE" + " IF EXISTS `cad_produtos_fornecedores`;":
            if line != "":
                count_end = count
                count_end = count_end - 3

    return count_begin, count_end


def procProduto(begin, end, fileLines):
    #print("proc_produto")
    v_entrou = 0
    insertInto = "INSERT INTO"+" `cad_produtos`(id, nome_produto, cod_barra, unidade, inf_adicional, pontos, id_moeda, modo_estoque, grade, kit, id_tipo, vr_compra, vr_venda, vr_venda_2, min_estoque, estoque, inativo, aliq_ipi, inside_icms_ipi, id_class_fiscal, aliq_id_base_icms, origem_produto, fracionado) VALUES"
    produtosList = []
    for i in range(begin, end):
        newLine = fileLines[i].replace(");", ")").replace("),", ")")
        if v_entrou == 0:
            if newLine in insertInto:
                v_entrou = 1
                newLine = newLine.replace("INSERT INTO"+" `cad_produtos`(", "").replace(") VALUES", "").replace(", ", ",")
                procLine = procLineToList(newLine)
                produtosList.append(procLine)
        else:
            print(newLine)
            newLine = newLine.replace("   35,00", "35.00").replace("    330,00", "    330.00").replace(" 150,00",
                                      " 150.00").replace("25,80", "25.80").replace(",U-", ".U-")
            newLine = newLine.replace("0,00", "0.00").replace(",00", ".00").replace("0,0", "0.0").replace("220,'", "220")
            newLine = newLine.replace("(- ,", "(-.").replace("(-,", "(-.").replace(",P", ".P").replace(", P", " P")
            newLine = newLine.replace(",-P", "-P").replace(" , ", " ").replace(",P", "P").replace("   ,", "")
            newLine = newLine.replace("230,'", "230'").replace("A,", "A").replace("B,", "B").replace(" ,", "")
            newLine = newLine.replace("(,", "(.").replace(",P", "P").replace("G,'", "G'").replace("T,", "T.")
            newLine = newLine.replace(",',", "',")
            newLine = newLine.replace("(", "").replace(")", "").replace("'", "").replace(", ", ",")
            procLine = procLineToList(newLine)
            produtosList.append(procLine)
    return produtosList


def procLineToList(line):
    lineProc = []
    if line != '':
        id, nome_produto, cod_barra, unidade, inf_adicional, \
        pontos, id_moeda, modo_estoque, grade, kit, id_tipo, \
        vr_compra, vr_venda, vr_venda_2, min_estoque, estoque, \
        inativo, aliq_ipi, inside_icms_ipi, id_class_fiscal, \
        aliq_id_base_icms, origem_produto, fracionado = line.split(',')

        lineProc = [id, nome_produto, cod_barra, unidade, inf_adicional,
                    pontos, id_moeda, modo_estoque, grade, kit, id_tipo,
                    vr_compra, vr_venda, vr_venda_2, min_estoque, estoque,
                    inativo, aliq_ipi, inside_icms_ipi, id_class_fiscal,
                    aliq_id_base_icms, origem_produto, fracionado]

        return lineProc


class File:

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
