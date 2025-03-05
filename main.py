import tkinter
from tkinter import *
from tkinter import ttk

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"  # azul / blue
co5 = "#fff873"  # amarela / yellow
co6 = "#e85151"  # vermelha / red
co7 =  co4   # + verde
co8 = "#fcfbf7"
fundo = "#3b3b3b"  # preta / black

janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, stick=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, stick=NW)

app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co6 )
app_x.place(x=25, y=10)

app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_x.place(x=17, y=70)

app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_separador.place(x=110, y=20)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4 )
app_o.place(x=170, y=10)

app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_o.place(x=165, y=70)

app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_o_pontos.place(x=130, y=20)

# linhas verticais

app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co6 )
app_.place(x=90, y=15)

app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co6 )
app_.place(x=160, y=15)

# linhas horizontais

app_ = Label(frame_baixo, text='', width=190,  relief='flat', padx=2, pady=1,  anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co6 )
app_.place(x=30, y=63)

app_ = Label(frame_baixo, text='', width=190, relief='flat', padx=2, pady=1,  anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co6 )
app_.place(x=30, y=123)

# botoes na linha 0

b_0= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_0.place(x=30, y=15)

b_1= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_1.place(x=100, y=15)

b_2= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_2.place(x=170, y=15)

# botoes na linha 1

b_3= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_3.place(x=30, y=75)

b_4= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_4.place(x=100, y=75)

b_5= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_5.place(x=170, y=75)

# botoes na linha 2

b_6= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_6.place(x=35, y=135)

b_7= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_7.place(x=105, y=135)

b_8= Button(frame_baixo, text='', width=3, font=('Ivy 17 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co6 )
b_8.place(x=175, y=135)

# botao jogar

b_jogar= Button(frame_baixo, text='Jogar', width=10, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
b_jogar.place(x=85, y=210)


janela.mainloop()

#Teste Commit

