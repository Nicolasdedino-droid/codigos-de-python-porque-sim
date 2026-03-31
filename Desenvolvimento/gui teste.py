import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry('480x480')     
letra = tk.Label(janela, text='Calculadora!').pack(pady=45)


butao = tk.Button(janela, text='sair do programa.', command=janela.destroy).pack(side='bottom')



tk.mainloop()