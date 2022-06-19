'''
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
'''
from doctest import master
from tkinter.ttk import Progressbar

from windowsFuncitions import telaPrincipalFuncitions
import tkinter as tk


class TelaPrincipal(tk.Tk):
    # Método construtor da Janela Principal
    def __init__(self):
        tk.Tk.__init__(self)
        self.mensagem = None
        self.filename = None
        self.progress = None
        self.fontepadrao = ("Arial", "10")
        self.withdraw()
        self.scroll = None
        self.geometry('900x200')
        self.state('iconic')
        self.title("Conversor de dados")
        self.iconbitmap("./renovar.ico")

        # Main menus
        menubar = tk.Menu(self)
        fileMenu = tk.Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Abrir", command=telaPrincipalFuncitions.openFile)
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

        self.nomeLabel = tk.Label(self.FrameFirst, text="Arquivo", font=self.fontepadrao)
        self.nomeLabel.pack(side=tk.LEFT)

        self.entryFileName = tk.Entry(self.FrameFirst)
        self.entryFileName["width"] = 80
        self.entryFileName["font"] = self.fontepadrao
        filename = tk.StringVar()
        self.entryFileName["textvariable"] = filename
        self.entryFileName.pack(side=tk.LEFT)

        #Botão para selecionar o arquivo que sera processado.
        self.ButtonImage = tk.Button(self.FrameFirst)
        self.imgButtonImage = tk.PhotoImage(file='./pesquisar16.png')
        self.ButtonImage["image"] = self.imgButtonImage
        self.ButtonImage["text"] = "Pasta"
        self.ButtonImage["font"] = self.fontepadrao
        self.ButtonImage["width"] = 80
        self.ButtonImage["compound"] = tk.LEFT
        self.ButtonImage["command"] = lambda: filename.set(telaPrincipalFuncitions.openFile())
        self.ButtonImage.pack(side=tk.TOP)

#Frame 2 processamento do arquivo
        self.FrameSecond = tk.Frame(self)
        self.FrameSecond["padx"] = 40
        self.FrameSecond.pack()

        #Botão para processar o arquivo.
        self.ButtonProcessa = tk.Button(self.FrameSecond)
        self.imgButtonProc = tk.PhotoImage(file='./processar.png')
        self.ButtonProcessa["image"] = self.imgButtonProc
        self.ButtonProcessa["text"] = "Processar"
        self.ButtonProcessa["font"] = self.fontepadrao
        self.ButtonProcessa["width"] = 80
        self.ButtonProcessa["compound"] = tk.LEFT
        self.ButtonProcessa["command"] = lambda: telaPrincipalFuncitions.fileProc(filename.get())
        self.ButtonProcessa.pack(side=tk.TOP)

#Frame 3 processamento do arquivo
        self.FrameThird = tk.Frame(self)
        self.FrameThird["padx"] = 40
        self.FrameThird.pack()

        self.progress = tk.StringVar()
        self.progress.set(50)
        self.progressBar = Progressbar(self.FrameThird, maximum=100, orient=tk.HORIZONTAL, variable=self.progress)
        self.progressBar.grid(row=0, column=0, sticky=tk.W + tk.E)