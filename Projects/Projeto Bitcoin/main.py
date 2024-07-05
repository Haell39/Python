from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Colors -------------------

co0 = "#000000" #black
co1 = "#ffffff" #white
co2 = "#0000ff" #blue

fundo = "#484f60" 

# Criando Janela ------------

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

janela.mainloop()


# dividindo a janela em 2 frames --------------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)




frame_cima = Frame(janela, width=320, height=50, bg=co1, pady = 0, padx = 0, relief = "flat")
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady = 0, padx = 0, relief = "flat")
frame_baixo.grid(row=2, column=0, sticky=NW)


#configurando frame em cima -----------------





janela.mainloop()