import tkinter as tk
#Define a tela do programa
janela = tk.Tk()
janela.geometry('500x500')
janela.title('Cadastrar')
#---separar---

#Funçao que acompanha o botao de cadastrar
def logar():
    name = None
    password = None
    #Pegar conteudo da entrada
    global entrada_nome
    global entrada_senha
    pegar_nome = entrada_nome.get()
    pegar_senha = entrada_senha.get()
    
    #condicionais para login
    if pegar_nome == 'admin':
        #Bloco do nome de user
        nome_ver = tk.Label(janela, text='Nome correto!', font=('arial', 6))
        nome_ver.pack()
        nome_ver.place(x=565, y=75)
        #Atualizar o estado do nome
        name = True
            
    if pegar_senha == '123':
        #Bloco da senha do user'
        nome_ver = tk.Label(janela, text='Senha correta!', font=('arial', 6))
        nome_ver.pack()
        nome_ver.place(x=565, y=125)
        #Atualizar o estado da senha
        password = True
        
    #Programa termina depois do user achar o que eu pretendia    
    if name and password == True:
        janela.destroy()
        

#Apresentar o que é (Uma tela de login)
apresentar = tk.Label(janela, text='Login')
apresentar.pack()

#Componentes para indicar as entradas
indicar_nome = tk.Label(janela, text="Nome de usuário:")
indicar_senha = tk.Label(janela, text="Senha do usuário:")

indicar_nome.pack()
indicar_senha.pack()
#posicionar textos
indicar_nome.place(x=0, y=75)
indicar_senha.place(x=0, y=125)

#Entradas onde vai ter a resposta do user
global entrada_nome
global entrada_senha
entrada_nome = tk.Entry(janela)
entrada_senha = tk.Entry(janela, show='*')

entrada_nome.pack()
entrada_senha.pack()
#posicionar entradas
entrada_nome.place(x=235, y=75)
entrada_senha.place(x=235, y=125)

#botão para cadastrar
butone = tk.Button(janela, text="Cadastrar!", command=logar)
butone.pack()
butone.place(x=250, y=325)

#Manter o programa vivo
janela.mainloop()

