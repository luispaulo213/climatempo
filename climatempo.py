import tkinter
from tkinter import *
from tkinter import ttk


################# cores ###############
cor0 = "#444466"  # Preto
cor1 = "#feffff"  # branco
cor2 = "#6f9fbd"  # azul


fundo_dia ="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"


fundo = fundo_dia

janela = Tk()
janela.title('App metereologia')
janela.geometry('320x350')
janela.configure(bg=fundo)

################# Frames ####################

#Separa a janela do fechar#
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

#frame top - onde pesquisa a cidade
#frame corpo - onde mostraremos dados da api
frame_top = Frame(janela, width=320, height=50, bg=cor1, pady=0, padx=0 )
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0 )
frame_corpo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use('clam')


cityinput = Entry(frame_top,width=17,justify='left',font=('Comic Sans MS',14),highlightthickness=1,relief="solid")
cityinput.place(x=25,y=10)

buttonsend = Button(frame_top,text='ver clima',bg=cor1,fg=cor2,justify='center',font=('Comic Sans MS',14),relief='raised',overrelief=RIDGE)
buttonsend.place(x=220,y=5)

textcity = Label(frame_corpo,text='Campo Mourão,Brasil/américa do sul',anchor='center',bg=fundo,fg=cor1,justify='left',font=('Comic Sans MS',14))
textcity.place(x=10,y=4)

textdate = Label(frame_corpo,text='08/12/2023-18:57:19',anchor='center',bg=fundo,fg=cor1,justify='left',font=('Comic Sans MS',14))
textdate.place(x=10,y=54)

janela.mainloop()