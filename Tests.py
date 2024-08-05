from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Colors -------------------
co0 = "#000000"  # black
co1 = "#ffffff"  # white
co2 = "#0000ff"  # blue

fundo = "#484f60"  

# Criando Janela ------------
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

# Dividindo a janela em 2 frames ----------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=2, column=0, sticky=NW)

# Configurando frame em cima -----------------
imagem = Image.open('D:/GitHub Desktop/Python-EXE-1/Projects/Projeto Bitcoin/bitcoin.png')
imagem = imagem.resize((30, 30), Image.Resampling.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, bg=co1, relief="flat")
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text="Bitcoin Price Tracker", bg=co1, relief="flat", anchor="center", font=('Arial, 20'), fg=co2)
l_nome.place(x=50, y=5)

# Configurando frame em baixo -----------------
l_cotacao = Label(frame_baixo, text="Cotação Atual: 1₿ = $58207,80 ", bg=fundo, relief="flat", anchor="center", font=('Garuda, 15'), fg=co1)
l_cotacao.grid(row=0, column=0, sticky=NW, padx=0, pady=10, ipadx=0, ipady=0)

# Adicionando linha divisória
ttk.Separator(frame_baixo, orient=HORIZONTAL).grid(row=1, column=0, columnspan=2, sticky='ew', pady=10)


l_cotacao = Label(frame_baixo, text="Cotação Atual: 1₿ = $58207,80 ", bg=fundo, relief="flat", anchor="center", font=('Garuda, 15'), fg=co1)
l_cotacao.grid(row=0, column=0, sticky=NW, padx=0, pady=10, ipadx=0, ipady=0)

l_cotacao = Label(frame_baixo, text="Cotação Atual: 1₿ = $58207,80 ", bg=fundo, relief="flat", anchor="center", font=('Garuda, 15'), fg=co1)
l_cotacao.grid(row=0, column=0, sticky=NW, padx=0, pady=10, ipadx=0, ipady=0)

l_cotacao = Label(frame_baixo, text="Cotação Atual: 1₿ = $58207,80 ", bg=fundo, relief="flat", anchor="center", font=('Garuda, 15'), fg=co1)
l_cotacao.grid(row=0, column=0, sticky=NW, padx=0, pady=10, ipadx=0, ipady=0)




# Aqui você pode adicionar mais widgets nos frames criados

# Chamando o mainloop
janela.mainloop()
