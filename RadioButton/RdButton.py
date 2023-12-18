import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

frame = tk.Tk()
frame.geometry("350x300")
frame.resizable(False, False)
frame.title("Exemplo radio button")
#frame.tk.call("wm", "iconphoto", frame._w, tk.PhotoImage(file = "86796219-icon-photo-camera-in-simple-black-and-white-vector-image.png"))

def mostarEscolha():
    showinfo(title = "Resultado", message = f"Você esvolheu {tam_selecionado.get()}")

tam_selecionado = tk.StringVar(frame, value = "M")

tamanhos = (("Pequeno", "P"), ("Médio", "M"), ("Grande", "G"), ("Extra Grande", "XG"), ("Extra Extra Grande", "XXG"))

lblPergunta = ttk.Label(text = "Escolha o tamanho: ")
lblPergunta.pack(fill = "x", padx = 5, pady = 5)

for tamanho in tamanhos:
    rd = ttk.Radiobutton(frame, text = tamanho[0], value = tamanho[1], variable = tam_selecionado)
    rd.pack(fill = "x", padx = 5, pady = 5)



btnEscolha = ttk.Button(frame, text = "Ler tamanho", command = mostarEscolha)
btnEscolha.pack(fill = "x", padx = 5, pady = 5)


frame.mainloop()