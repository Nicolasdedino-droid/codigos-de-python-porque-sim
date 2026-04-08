import re
import tkinter as tk

janela = tk.Tk()
janela.title("email")
janela.geometry('600x500')

texto = tk.Label(janela, text='Digite seu gmail.', font=('Arial', 19))
texto.pack()

entrada = tk.Entry(janela)
entrada.pack()

def verificaçao():
    valor = entrada.get()
    
    if re.search(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.gmail', valor):
        valido = tk.Label(janela, text="Email válido!",font=('Arial', 5))
        valido.pack()
        valido.place(x=92, y=90)
        valido.config(text="Email válido!")
        fim = tk.Label(janela, text="Fim do programa!\nObrigado pela a\ncolaboração!\n:)")
        fim.pack()
        
    else:
        invalido = tk.Label(janela, text='Email inválido', font=('Arial', 5))
        invalido.pack()
        invalido.place(x=75, y=85)
        invalido.after(1000, invalido.destroy)


butone = tk.Button(janela, text='Verificar', command=verificaçao)
butone.pack()

janela.mainloop()
