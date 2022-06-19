import tkinter
from tkinter import *


class MinhaGUI:
    def __init__(self):
        # Criando a janela principal
        self.janela_principal = Tk()
        self.janela_principal.geometry('900x200')

        # Criando os frames
        self.FrameFirst = tkinter.Frame(master)
        self.FrameFirst["padx"] = 20
        self.FrameFirst.pack()

        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)

        # Criando os labels
        self.label1 = Label(self.frame_cima, text='To no frame de cima!')
        self.label2 = Label(self.frame_baixo, text='To no frame de baixo!')

        # Posicionando os labels nos frames
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        # Posicionando o frame
        self.frame_cima.pack()
        self.frame_baixo.pack()

        # Fazer o Tkinter exibir o looping da janela
        mainloop()


minha_gui = MinhaGUI()



#from tkinter import *
#from tkinter.ttk import *

#root = Tk()
#progress = Progressbar(root, orient=HORIZONTAL,
#                       length=100, mode='indeterminate')


#def bar():
#    import time
#    progress['value'] = 20
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 40
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 50
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 60
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 80
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 100
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 80
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 60
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 50
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 40
#    root.update_idletasks()
#    time.sleep(0.5)

#    progress['value'] = 20
#    root.update_idletasks()
#    time.sleep(0.5)
#    progress['value'] = 0


#progress.pack(pady=10)
#Button(root, text='Start', command=bar).pack(pady=10)
#mainloop()