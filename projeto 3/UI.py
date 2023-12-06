import tkinter as tk
window = tk.Tk()
window.title("TKInter Py App")
window.geometry("300x300")
newLabel = tk.Label(text = "Olá, TKInter")
newLabel.grid(column = 1, row = 3)
newLabel.pack(anchor = "center")
window.mainloop()