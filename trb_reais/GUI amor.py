import tkinter as tk
from tkinter import *

def main():
    
    def clicker():
        global texto
        texto.config(text='Eu te amo!!')
      
  
    janela = tk.Tk()
    janela.title('Mensagem especial')
    janela.geometry('480x480')
    
    butone = tk.Button(janela, text='Clique-me!', command=clicker).place(y = 645, x=265)
    
    
    global texto
    texto = tk.Label(janela, text='')
    
    texto.pack(pady=25)
     
    destroy = tk.Button(janela, text='Fechar programa', command=janela.destroy)
    destroy.place(x=225, y=1375)
    
    tk.mainloop()
    
if __name__ == '__main__':
    main()