import tkinter as tk
from tkinter import messagebox

#Tudo sobre janela
janela = tk.Tk()
janela.title = ("Criador")
janela.geometry("600x500")
#---separar!~---

#!~Texto de apresentação~!
texto_apr = tk.Label(janela, text="Criar textos!", font=("Arial", 19))
texto_apr.pack()
#Separador!!+

#A caixa de texto#
entrada = tk.Entry(janela)
entrada.pack()
entrada.place(x=0, y=300, width=900, height=500)

# Separador!~

#Comandos do botão
def criador():
    pegar = entrada.get()
    with open("tkinter.txt", "a") as file:
        file.write(f"{pegar}\n")
    messagebox.showinfo("Aviso!", "Arquivo já foi criado.")
    
def leitura():
    lista = []
    #Abre arquivo
    with open("tkinter.txt") as file:
        for coisas in file:
            lista.append(coisas)
    #Gerar texto após a leitura

        l = tk.Label(janela, text=lista)
        l.pack()
        def destruir():
            l.destroy()
        l.after(5000, destruir)                                     
# Fim dos comandos
  
#Butone
butone = tk.Button(janela, text="Criar arquivo!", command=criador)
butone.pack()
butone.place(x=239, y = 910)

#Sair do programa
destruir = tk.Button(janela, text="fechar programa", command=janela.destroy)
destruir.pack()
destruir.place(x=219, y = 1000)

#ler o arquivo
ler = tk.Button(janela, text="Ler arquivo", command=leitura)
ler.pack()

janela.mainloop()
