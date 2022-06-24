"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""

from tkinter import filedialog, messagebox
from functions import arquivos


def on_close():
    quit()


def openFile():
    filename = filedialog.askopenfilename(initialdir="./",
                                          title="Selecione o arquivo",
                                          filetypes=(("Arquivo texto",
                                                      "*.*"),
                                                     ("Todos arquivos",
                                                      "*.*")))
    return filename


def fileProc(filename):
    filename = filename
    extension = ''
    encoding = 'utf-8'
    openType = 'r'

    if filename != "":
        # Open File
        arquivos.File(filename, extension, encoding, openType)
        # Valid the encoding file
        file = arquivos.openFile(filename, arquivos.returnEncoding(filename, "Windows-1252"))
        # process the file to validate where the product lines start and end
        count_begin, count_end = arquivos.procLine(file)
        # process the product line
        arquivos.procProduto(count_begin, count_end, file)
        print(count_begin, count_end)
    else:
        messagebox.showwarning("Alerta", "Nenhum arquivo selecionado!")
