import tkinter as tk

#Define a entrada

def entrar():
    pegar = entrada.get()
    tex.config(text=pegar)

#criar janela
janela = tk.Tk()
janela.title('Teste')
janela.geometry('300x300')
            
# Apresentando a idéia com uma introdução

texto = tk.Label(janela, text='Escreve o que quiser! :D').pack(pady=75)

#Cria a entrada
entrada = tk.Entry(janela)
entrada.pack()
tex = tk.Label(janela, text='')
tex.pack()

#Faz um botão que gera o conteúdo da entrada

fazer = tk.Button(janela, text='Gerar texto!', command=entrar)
fazer.pack()


#Sair do programa
sair = tk.Button(janela, text='Sair do programa', command=janela.destroy).pack(pady=225)

janela.mainloop()