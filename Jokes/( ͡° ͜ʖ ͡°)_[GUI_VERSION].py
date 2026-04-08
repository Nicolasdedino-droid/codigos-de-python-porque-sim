import tkinter as tk
from tkinter import messagebox
import webbrowser

#Janela...
janela = tk.Tk()
janela.title("MUAHAAH")
janela.geometry("500x400")
#Hm

#Heheh
texto = tk.Label(janela, text="Aperte o botão abaixo!\n:>", font=("Arial", 16))
texto.pack()
#>:)

#HHSHAHAHAHA
def trololo():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")   
def UHH():
    butone.destroy()
    texto.destroy()
    tk.Label(janela, text="...").pack()
    tk.Label(janela, text="Você estragou a minha brincadeira, sabe de algo?\nnão preciso da\nPORCARIA de um butão para te enganar...").pack()
    abondonado.destroy()
    
def abrir():
    webbrowser.open("https://youtu.be/wcinzmfZeCc?si=Di5ALLZUttNMGFhZ")           
#...
butone = tk.Button(janela, text="Me aperte!", command=trololo)
butone.pack()

abondonado = tk.Button(janela, text="Botão abondonado.", command=UHH)
abondonado.pack()
abondonado.place(x=0, y=499)

janela.after(15000, abrir)

#Já sabemos a onde isso vai chegar...
janela.mainloop()