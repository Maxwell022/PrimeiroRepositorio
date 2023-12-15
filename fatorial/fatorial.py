import tkinter as tk

def calculo():
    n = int(campoText.get())
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i += 1
    inverted.config(text=f"O valor de {n}! = {fat}")
    limpar()

def limpar():
    lista = [campoText]

    for input in lista:
        input.delete(0, tk.END)


janela = tk.Tk()
janela.geometry("320x180")
janela.title("Text Inverter")
janela.resizable(False, False)


text = tk.Label(text = "Digite o número ", height = 2, font = ("comic sans", 14, "bold"))
text.grid(column = 0, row = 0)


inverted= tk.Label(height = 2, font = ("comic sans", 14, "bold"))
inverted.grid(column = 1, row = 1)


campoText = tk.Entry(width = 12, font = ("comic sans", 14))
campoText.grid(column = 1, row = 0)


bInverter = tk.Button(janela, text = "OK", bg = "yellow", command = calculo, width = 10, font = ("comic sans", 14, ))
bInverter.grid(column = 1, row = 2)

bLimpar = tk.Button(janela, text = "Limpar", command = limpar, width = 10, font = ("comic sans", 14))
bLimpar.grid(column = 0, row = 2)

janela.mainloop()