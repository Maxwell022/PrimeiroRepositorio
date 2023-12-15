import tkinter as tk

def calculo():
    n = int(campoText.get())
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i += 1
    inverted.config(text=f"O valor de {n}! = {fat}")


janela = tk.Tk()
janela.geometry("500x500")
janela.title("Text Inverter")
janela.resizable(False, False)


text = tk.Label(text = "Digite o número ", height = 2, font = ("comic sans", 14, "bold"))
text.grid(column = 0, row = 0)


inverted= tk.Label(height = 2, font = ("comic sans", 14, "bold"))
inverted.grid(column = 1, row = 1)


campoText = tk.Entry(width = 12, font = ("comic sans", 14))
campoText.grid(column = 1, row = 0)


bInverter = tk.Button(janela, text = "OK", command = calculo, width = 10, font = ("comic sans", 14))
bInverter.grid(column = 1, row = 2)

janela.mainloop()