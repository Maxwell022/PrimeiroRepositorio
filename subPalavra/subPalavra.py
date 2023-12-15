import tkinter as tk

def substituir():
    frase= campoFrase.get()
    alvo = campoAlvo.get()
    substituto = campoSubstituto.get()
    frase = frase.replace(alvo, substituto)
    inverted["text"] = frase

    
def limpar():
    lista = [campoFrase, campoSubstituto, campoAlvo]
    inverted["text"] = "Resultado"
    for input in lista:
        input.delete(0, tk.END)


janela = tk.Tk()
janela.geometry("500x300")
janela.title("Text Inverter")
janela.resizable(False, False)


alvo = tk.Label(text = "Letra alvo", height = 2, font = ("comic sans", 14, "bold"))
alvo.grid(column = 0, row = 0)

substituto = tk.Label(text = "substituto", height = 2, font = ("comic sans", 14, "bold"))
substituto.grid(column = 3, row = 0)

frase = tk.Label(text = "Frase", height = 2, font = ("comic sans", 14, "bold"))
frase.grid(column = 0, row = 2)

inverted= tk.Label(text = "Resultado",height = 2, font = ("comic sans", 14, "bold"))
inverted.grid(column = 3, row = 3)

#campos

campoFrase = tk.Entry(width = 12, font = ("comic sans", 14))
campoFrase.grid(column = 0, row = 3)

campoAlvo = tk.Entry(width = 12, font = ("comic sans", 14))
campoAlvo.grid(column = 0, row = 1)

campoSubstituto = tk.Entry(width = 12, font = ("comic sans", 14))
campoSubstituto.grid(column = 3, row = 1)
#bu
bInverter = tk.Button(janela, text = "Trocar", bg = "yellow", command = substituir, width = 10, font = ("comic sans", 14, ))
bInverter.grid(column = 1, row = 2)

bLimpar = tk.Button(janela, text = "Limpar", command = limpar, width = 10, font = ("comic sans", 14))
bLimpar.grid(column = 0, row = 4)

janela.mainloop()