# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""
from doctest import master
from tkinter.ttk import Progressbar

from windowsFuncitions import telaPrincipalFuncitions
import tkinter as tk


class TelaPrincipal(tk.Tk):
    # Método construtor da Janela Principal
    def __init__(self):
        tk.Tk.__init__(self)
        self.mensagem = None
        self.filenameSql = None
        self.filenameXml = None
        self.progress = None
        self.fontepadrao = ("Arial", "10")
        self.withdraw()
        self.scroll = None
        self.geometry('900x200')
        self.state('iconic')
        self.title("Conversor de dados")
        self.iconbitmap("./image/renovar.ico")

        # Main menus
        menubar = tk.Menu(self)
        fileMenu = tk.Menu(menubar, tearoff=0)
        #fileMenu.add_command(label="Abrir", command=lambda: filename.set(telaPrincipalFuncitions.openFile()))
        fileMenu.add_command(label="Salvar", command="self.model.donothing")
        fileMenu.add_command(label="Salvar como...", command="self.model.donothing")
        fileMenu.add_command(label="Fechar", command=telaPrincipalFuncitions.on_close)
        fileMenu.add_separator()
        fileMenu.add_command(label="Sair", command=quit)
        menubar.add_cascade(label="Arquivo", menu=fileMenu)

        helper = tk.Menu(menubar, tearoff=0)
        helper.add_command(label="Sobre", command="self.model.about")
        menubar.add_cascade(label="Ajuda", menu=helper)

        self.config(menu=menubar)
        # self.state('zoomed')

# Frame 1 processamento do arquivo
        self.FrameFirst = tk.Frame(self)
        self.FrameFirst["padx"] = 20
        self.FrameFirst.pack()

        self.nomeLabelSql = tk.Label(self.FrameFirst, text="Caminho SQL", font=self.fontepadrao)
        self.nomeLabelSql.pack(side=tk.LEFT)

        self.entryFileNameSql = tk.Entry(self.FrameFirst)
        self.entryFileNameSql["width"] = 80
        self.entryFileNameSql["font"] = self.fontepadrao
        filenameSql = tk.StringVar()
        self.entryFileNameSql["textvariable"] = filenameSql
        self.entryFileNameSql.pack(side=tk.LEFT)

        #Botão para selecionar o arquivo que sera processado.
        self.ButtonImageSql = tk.Button(self.FrameFirst)
        self.imgButtonImageSql = tk.PhotoImage(file='./image/folderFile.png')
        self.ButtonImageSql["image"] = self.imgButtonImageSql
        self.ButtonImageSql["text"] = "Arquivo"
        self.ButtonImageSql["font"] = self.fontepadrao
        self.ButtonImageSql["width"] = 80
        self.ButtonImageSql["compound"] = tk.LEFT
        self.ButtonImageSql["command"] = lambda: filenameSql.set(telaPrincipalFuncitions.openFile(1))
        self.ButtonImageSql.pack(side=tk.TOP)

# Frame 2 processamento do arquivo
        self.FrameSecond = tk.Frame(self)
        self.FrameSecond["padx"] = 20
        self.FrameSecond.pack()

        self.nomeLabelXml = tk.Label(self.FrameSecond, text="Caminho XML", font=self.fontepadrao)
        self.nomeLabelXml.pack(side=tk.LEFT)

        self.entryFileNameXml = tk.Entry(self.FrameSecond)
        self.entryFileNameXml["width"] = 80
        self.entryFileNameXml["font"] = self.fontepadrao
        filenameXml = tk.StringVar()
        self.entryFileNameXml["textvariable"] = filenameXml
        self.entryFileNameXml.pack(side=tk.LEFT)

        # Botão para selecionar o arquivo que sera processado.
        self.ButtonImageXml = tk.Button(self.FrameSecond)
        self.imgButtonImageXml = tk.PhotoImage(file='./image/folderOpen.png')
        self.ButtonImageXml["image"] = self.imgButtonImageXml
        self.ButtonImageXml["text"] = "Pasta"
        self.ButtonImageXml["font"] = self.fontepadrao
        self.ButtonImageXml["width"] = 80
        self.ButtonImageXml["compound"] = tk.LEFT
        self.ButtonImageXml["command"] = lambda: filenameXml.set(telaPrincipalFuncitions.openFile(2))
        self.ButtonImageXml.pack(side=tk.TOP)


#Frame 2 processamento do arquivo
        self.FrameThird = tk.Frame(self)
        self.FrameThird["padx"] = 40
        self.FrameThird.pack()

        #Botão para processar o arquivo.
        self.ButtonProcessa = tk.Button(self.FrameThird)
        self.imgButtonProc = tk.PhotoImage(file='./image/play-button.png')
        self.ButtonProcessa["image"] = self.imgButtonProc
        self.ButtonProcessa["text"] = "Processa SQL"
        self.ButtonProcessa["font"] = self.fontepadrao
        self.ButtonProcessa["width"] = 80
        self.ButtonProcessa["compound"] = tk.LEFT
        self.ButtonProcessa["command"] = lambda: telaPrincipalFuncitions.fileProc(filenameSql.get())
        self.ButtonProcessa.pack(side=tk.TOP)

#Frame 3 processamento do arquivo
        self.FrameFourth = tk.Frame(self)
        self.FrameFourth["padx"] = 40
        self.FrameFourth.pack()

        self.progress = tk.StringVar()
        self.progress.set(50)
        self.progressBar = Progressbar(self.FrameFourth, maximum=100, orient=tk.HORIZONTAL, variable=self.progress)
        self.progressBar.grid(row=0, column=0, sticky=tk.W + tk.E)