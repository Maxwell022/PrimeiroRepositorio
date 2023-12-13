import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as mb

def limpar():
    lista = [campoNome, campoAno]

    for input in lista:
        input.delete(0, tk.END)

def getInput():
    try:    
        humano = Pessoa(campoNome.get(), int(campoAno.get()))
        limpar()
        mb.showinfo(title = "Resultado", message = f"Olá {humano.nome}, você tem {humano.idade()} anos de idade")
    except ValueError:
        mb.showerror(title = "Erro!", message = f"Informe apenas números no campo ano")

janela = tk.Tk()
janela.geometry("280x180")
janela.title("Age Calculator")

nome = tk.Label(text = "Nome:", height = 2, font = ("comic sans", 14, "bold"))
nome.grid(column = 0, row = 1)


ano = tk.Label(text = "Ano:", height = 2, font = ("comic sans", 14, "bold"))
ano.grid(column = 0, row = 2)

#Entradas

campoNome = tk.Entry(width = 12, font = ("comic sans", 14))
campoNome.grid(column = 1, row = 1)

campoAno = tk.Entry(width = 12, font = ("comic sans", 14))
campoAno.grid(column = 1, row = 2)

#Butões

bCalcular = tk.Button(janela, text = "OK", command = getInput, width = 10, font = ("comic sans", 14))
bCalcular.grid(column = 1, row = 5)

bLimpar = tk.Button(janela, text = "Limpar", command = limpar, width = 10, font = ("comic sans", 14))
bLimpar.grid(column = 0, row = 5)


janela.mainloop()