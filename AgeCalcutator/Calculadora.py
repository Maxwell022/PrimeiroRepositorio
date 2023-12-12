import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as mb

def limpar():
    lista = [campoNome, campoDia, campoMes, campoAno]

    for input in lista:
        input.delete(0, tk.END)

def getInput():
    humano = Pessoa(campoNome.get(), dt(int(campoAno.get()), int(campoMes.get()), int(campoDia.get())))

    mb.showinfo(title = "Resultado", message = humano.idade())

def Calcular():
    pass

#

janela = tk.Tk()
janela.geometry("320x320")
janela.title("Age Calculator")

nome = tk.Label(text = "Nome:", height = 2, font = ("comic sans", 14, "bold"))
nome.grid(column = 0, row = 1)

dia = tk.Label(text = "Dia:", height = 2, font = ("comic sans", 14, "bold"))
dia.grid(column = 0, row = 2)

mes = tk.Label(text = "Mês:", height = 2, font = ("comic sans", 14, "bold"))
mes.grid(column = 0, row = 3)

ano = tk.Label(text = "Ano:", height = 2, font = ("comic sans", 14, "bold"))
ano.grid(column = 0, row = 4)

#Entradas

campoNome = tk.Entry(width = 12, font = ("comic sans", 14))
campoNome.grid(column = 1, row = 1)

campoDia = tk.Entry(width = 12, font = ("comic sans", 14))
campoDia.grid(column = 1, row = 2)

campoMes = tk.Entry(width = 12, font = ("comic sans", 14))
campoMes.grid(column = 1, row = 3)

campoAno = tk.Entry(width = 12, font = ("comic sans", 14))
campoAno.grid(column = 1, row = 4)

#Butões

bCalcular = tk.Button(janela, text = "OK", command = getInput, width = 10, font = ("comic sans", 14))
bCalcular.grid(column = 1, row = 5)

bLimpar = tk.Button(janela, text = "Limpar", command = limpar, width = 10, font = ("comic sans", 14))
bLimpar.grid(column = 0, row = 5)


janela.mainloop()