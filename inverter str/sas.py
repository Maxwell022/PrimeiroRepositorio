import tkinter as tk

def inverter(): 
    frase = campoText.get()
    invertida = " ".join(palavra[::-1] for palavra in frase.split())
    inverted.config(text= invertida)
    

janela = tk.Tk()
janela.geometry("500x500")
janela.title("Text Inverter")
janela.resizable(False, False)


text = tk.Label(text = "Enter a word: ", height = 2, font = ("comic sans", 14, "bold"))
text.grid(column = 0, row = 0)


inverted= tk.Label(height = 2, font = ("comic sans", 14, "bold"))
inverted.grid(column = 1, row = 1)


campoText = tk.Entry(width = 12, font = ("comic sans", 14))
campoText.grid(column = 1, row = 0)


bInverter = tk.Button(janela, text = "OK", command = inverter, width = 10, font = ("comic sans", 14))
bInverter.grid(column = 1, row = 2)



janela.mainloop()