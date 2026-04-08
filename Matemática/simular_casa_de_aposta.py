import random
import sys
sys.path.append("/storage/emulated/0/Python/Módulos")
from Tratar_erros import intinput
#Simulador de apostas CLI

def main():
    #Cadastrar na simulação!
    while True:
        nome = input("Digite seu nome: ").strip()
        if nome == '':
            break
        idade = intinput("Digite a sua idade: ")
        #Verficar idade
        if idade < 18:
            print("Você não poderá entrar!")
            break
        elif idade > 100:
            print("Não.")
        else:
            aposta()
            
 # Funções e engrenagens por trás           

def manipular(valor):
    # Função que incentiva a continuar apostando
    valor_positivo = round(random.randint(valor // 8, valor // 7))
    return valor_positivo
    
def ganhar_vantagem(valor):
    #Função que representa a perda e que a casa sempre ganha
    valor_negativo = random.randint(valor //7, valor // 3)
    return valor_negativo    
    
def dados():
    global dinheiro
    ganho_total = ganhar_vantagem(dinheiro)
    percas = manipular(dinheiro)
    with open("Dados_da_casa.txt", "a") as file:
        file.write(f"Ganhos da casa: {ganho_total} e percas da casa: {percas}\n")
                                                                     
def aposta():
    global dinheiro
    #Usuário escolhe a quantidade e a casa gerará um resultado em cima disso
    dinheiro = intinput("Digite a quantidade de dinheiro que você irá gastar: ")
    preescolha = [True, False]
    
    print(f"Dinheiro atual: {dinheiro}")          
    while True:
        escolher = random.choice(preescolha)
        #Ativa as funções psicológicas que mantém o usuário preso e querer mais "dinheiro"
        if dinheiro < 100:
            #O jogo encerra quando o dinheiro do usuário é menor que 100.
            sys.exit("Valor minímo é 100.")
            
        if escolher == True:
            ganho = manipular(dinheiro)
            situar = input("Quer apostar?(Y/n)\n").lower()
            #Dilema moral do jogador:
            if situar == "y":
                dinheiro += ganho
                print(f"Valor atual: {dinheiro}")
                continue
            elif situar == "n":
                dados()
                sys.exit("Tchau!")
                
        elif escolher == False:
            perca = ganhar_vantagem(dinheiro)
            brecha = input("Quer apostar?(Y/n)\n").lower()
            #Dilema moral do jogador:
            if brecha == "y":
                dinheiro -= perca
                print(f"Valor atual: {dinheiro}")
                continue
            elif brecha == "n":
                dados()
                sys.exit("Tchau!")
        
if __name__ == "__main__":
    main()        