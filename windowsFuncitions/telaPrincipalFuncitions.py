# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""

from tkinter import filedialog, messagebox
from functions import arquivosSql
from functions import arquivosXml


def on_close():
    quit()


def openFile(Botao):
    if Botao == 1:
        title = "Selecione o arquivo SQL"
        filetypes = "Arquivo SQL"
        types = "*.sql"
        filename = filedialog.askopenfilename(initialdir="./",
                                              title=title,
                                              filetypes=((filetypes,
                                                          types),
                                                         ("Todos arquivos",
                                                          "*.*")))

    if Botao == 2:
        title = "Selecione o arquivo XML"
        filetypes = "Arquivo XML"
        types = "*.xml"
        filename = filedialog.askdirectory()

    return filename


def fileProc(filenameSQL, filenameXML):
    filenameSQL = filenameSQL
    filenameXML = filenameXML
    extension = ''
    encoding = 'utf-8'
    openType = 'r'

    if filenameSQL != "" and filenameXML != "":
        if filenameSQL != "":
            # Open File
            #arquivosSql.File(filenameSQL, extension, encoding, openType)
            # Valid the encoding file
            file = arquivosSql.openFileSql(filenameSQL, arquivosSql.returnEncoding(filenameSQL, "Windows-1252"))
            # process the file to validate where the product lines start and end
            count_begin, count_end = arquivosSql.procLineSql(file)
            # process the product line
            arquivosSql.procProduto(count_begin, count_end, file)
            print(count_begin, count_end)
        else:
            messagebox.showwarning("Alerta", "Arquivo SQL não foi selecionado!")

        if filenameXML != "":
            dirXml, subXml, arquXml = arquivosXml.getFileXml(filenameXML, "teste")
            arquivosXml.procLineXml(dirXml, subXml, arquXml)

        else:
            messagebox.showwarning("Alerta", "Arquivo XML não foi selecionado!")
    else:
        messagebox.showwarning("Alerta", "Nenhum arquivo foi selecionado!")
