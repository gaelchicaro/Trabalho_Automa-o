import pandas as pd
import pyautogui as pg
import pyperclip as pc
import time
from datetime import datetime
from tkinter import simpledialog

biblioteca = simpledialog.askstring( "Biblioteca", "Digite o nome da biblioteca:")
print(biblioteca)
#Todo o bloco do tkinter foi o chat que fez, pois 
# eu não queria usar o input para deixar mais interativo pro usuário




livros = pd.read_excel("livros.xlsx")
hoje = datetime.now()
data_formatada = hoje.strftime('%d/%m/%Y')
#Uso de Ia para inserir a data

pg.press("win")
time.sleep(0.5)
pg.write("writer")
pg.press("enter")
time.sleep(1)

pg.press("enter")
pg.hotkey("ctrl", "b")
pg.write("Ficha de Livros")
time.sleep(0.1)
pg.hotkey("ctrl", "b")
pg.press("enter")
for livro, linha in livros.iterrows():
    
    #variaveis
    nome = linha["Nome"]
    autor = linha["Autor"]
    ano = str(linha["Ano_lancamento"])
    genero = linha["Genero"]

# Uso de Ia para apernder a escrever com acentos usando o pyperclip
    pc.copy(nome)
    pg.hotkey("ctrl", "u")
    pg.hotkey('ctrl','v')
    pg.hotkey("ctrl", "u")
    pg.press("enter")
    time.sleep(0.3)
    pc.copy(autor)
    pg.hotkey('ctrl','v')
    pg.press("enter")
    time.sleep(0.3)
    pc.copy(ano)
    pg.hotkey('ctrl','v')
    pg.press("enter")
    time.sleep(0.3)
    pc.copy(genero)
    pg.hotkey('ctrl','v')
    pg.press("enter")
    pg.press("enter")
    time.sleep(0.3)

time.sleep(0.5)
pg.write("Biblioteca provedora: ")
pg.write(biblioteca)
pg.press('enter')
pg.write(data_formatada)
time.sleep(0.5)
pg.hotkey("ctrl", "s")
pg.write("Ficha_de_livros")
pg.press("enter")