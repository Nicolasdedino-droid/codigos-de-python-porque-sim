import sys
import os
import time

roxo = "\033[0;35m"
branco = "\x1b[37m"
red = "\033[0;31m"

introdução = '''Terminal Linux no android!!! ;P

Bem vindo ao terminal do Linux no Android...baseado no Termux, este programa é uma sátira e não deve ser levado à sério, mas se você for iniciante em terminais, pode acabar...Well. . .

E até profissonais podem xingar a minha lógica de raciocínio, então digite "help" para mais informações'''

print(introdução)

def main():
    raiva = 0
    while True:
        comando = input(">>> ")
    
        if comando == "help":
            ajuda()
    
        elif comando == "echo":
            pergunta = input("O que deseja imprimir?\n>>> ") 
            print(pergunta)
       
        elif comando == "mkdir":
            nome = input("Qual o nome do novo diretório?\n")
            try:
                os.mkdir(nome)
            except FileNotFoundError:
                print(roxo, 'Diretório não encontrado;/+', red, "FileNotFoundError", branco)
        
                
        else:
            if raiva >1:
                processo_final()
                print("Você cometeu o mesmo.erro...huh? Sabe de algo...apenas olha os arquivos do seu celular... =)")
                sys.exit()
            else:
                processo_1()
                processo_2()
                raiva += 2
            
            
                
            
            
            
            
            
def ajuda():
       print('''Olá! Você deve estar se perguntando se isso é algo profissonal...e eu digo que não! ;D
       
Este programa em si foi feito na zueira e só tem 3 comandos de verdade:
       
       digitando "echo" vai pedir para você digitar algo e gerar um texto
       
       digitando "mkdir" vai (obviamente) criar um diretório, onde você pode escolher o nome.
       
       digitando "help" vai gerar uma ajuda. você já sabe disso -_-
       
       
O especial desse programa é que se você digitar outra coisa...pode gerar alguns..."inimigos" desnecessários no seu dispotivo!''')

def dialogo(tempo, texto):
    for palavras in texto:
        sys.stdout.write(palavras)
        sys.stdout.flush()
        time.sleep(tempo)
    print()
       

def processo_1():
    dialogo(0.04, "!ATENÇÃO!: Aqui pode ter algumas ofensas gratuitas, quem quiser continuar, continue então. Mas eu ainda gosto de você! ;D")
    time.sleep(5.5)
    os.system('cls' if os.name == "nt" else "clear")
    
    dialogo(1, "V-O-C-Ê...")
    
    dialogo(0.02, "Você...QUEM MANDOU SER UM INICIANTE TÃO RUIM?! Eu literalmente escrevi uma ajuda que você poderia ler, e você simplesmente errou o bash mais simples do mundo...EU NÃO SOU PAGO O SUFICIENTE PARA ATURAR ANALFABETO!!")
    
    dialogo(0.5, "NÃO MESMO...")
    
    dialogo(0.05, "Pessoas como você nem se quer merecem o acesso à tecnologia...claramente se você NÃO consegue LER a bosta da introdução, imagina para fazer comandos...isso é para vida! E não quero ouvir nenhuma desculpa...")
    
def processo_2():
    with open("GET_OUT.txt", "a") as danger:
        for _ in range(9999):
            danger.write("INÚTIL!!!\n")    
            
def processo_final():
    letras = ["Hahahah", "Buahahah", "Muahahahaha", "Sou chato mesmo, que nem você", "KKKKKK"]
    for palavras in letras:
        os.mkdir(palavras)
        with open(f"{palavras}.txt", "a") as chatice:
            chatice.write("LEIA-ME E PERDE MAIS TEMPO")


if __name__ == "__main__":
       main()
       