import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import requests
from datetime import datetime
import json
import pycountry_convert as pc 
import pytz
 
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


#Separa a janela do fechar#
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

#frame top - onde pesquisa a cidade
#frame corpo - onde mostraremos dados da api
frame_top = Frame(janela, width=320, height=50, bg=cor1, pady=0, padx=0 )
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0 )
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


#funcao info
def info ():
    key = "170dccace6e532e5a666a96bcb963e9e"
    city = ''
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,key)
    r = requests.get(api_link)
    dados = r.json()
    print(dados)
    
    pais_codigo = dados['sys']['country'] 
    fusohorario = pytz.country_timezones[pais_codigo] 
    pais_nome = pytz.country_names[pais_codigo]

    zona = pytz.timezone(fusohorario[0])
    zonahoras = datetime.now(zona)
    zonahoras = zonahoras.strftime('%m/%d/%Y/%H:%M:%S')

    tempo = dados['main']['temp']
    pressure = dados['main']['pressure']
    humidity = dados['main']['humidity']
    velocity = dados['wind']['speed']
    description = dados['weather'][0]['description']


    def countryToContinent(i):
        paisAlpha = pc.country_name_to_country_alpha2(i)
        paisContCode = pc.country_alpha2_to_continent_code(paisAlpha)
        paisContName = pc.convert_continent_code_to_continent_name(paisContCode)
        return paisContName
    continente = countryToContinent(city)
    #macumba sarava
    texto_cidade['text']=city+' -_- ' + pais_nome + ' -_- ' + continente

#input e botão
entrada_input = Entry(frame_top, width=17, justify='left', font=("", 14), highlightthickness=1, relief='solid')
entrada_input.place(x=25, y=10)
botao_ver = Button(frame_top,command=info ,text='ver', bg=cor1, fg=cor2,  justify='left', font=("Ivy 9 bold", 14), relief='raised', overrelief=RIDGE)
botao_ver.place(x=220, y=10) 

#label continente e pais
texto_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1,  justify='left', font=("Arial 14", 14))
texto_cidade.place(x=10, y=4) 

texto_data = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1,  justify='left', font=("Arial 10", 14))
texto_data.place(x=10, y=54) 



l_umidade = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 45 '), bg=fundo, fg=cor1)
l_umidade.place(x=10, y=100)

l_umidade_simbol = Label(frame_corpo, text="%", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 bold '), bg=fundo, fg=cor1)
l_umidade_simbol.place(x=85, y=110)

l_umidade_nome = Label(frame_corpo, text="umidade", height=1, padx=0, relief="flat", anchor="center", font=('Arial 8 '), bg=fundo, fg=cor1)
l_umidade_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text="Pressão", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=cor1)
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text="Velocidade do vento:", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=cor1)
l_velocidade.place(x=10, y=212)

# image = Image.open('istockphoto-1354219060-612x612.jpg').convert('RGB')
# image = image.resize((100, 100))
# image = ImageTk.PhotoImage(image)

# l_icon = Label(frame_corpo, image=image, bg=fundo)
# l_icon.place(x=190, y=70)

l_descricao = Label(frame_corpo, text="Nublado com nuvens", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=cor1)
l_descricao.place(x=170, y=190)



janela.mainloop()
