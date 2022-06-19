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
        arquivos.file(filename, extension, encoding, openType)
        file = arquivos.openFile(filename, arquivos.returnEncoding(filename, "Windows-1252"))
        arquivos.proc_Line(file)
        #print(file)
    else:
        messagebox.showwarning("Alerta", "Nenhum arquivo selecionado!")