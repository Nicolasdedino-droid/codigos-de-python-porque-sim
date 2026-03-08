import random
import sys
import os
import time

pontuacao = 0
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
soma = num1 + num2

print(f"Qual a soma entre {num1} e {num2}? ({num1} + {num2})")

while True:
    try:
        resposta = int(input("Digite a soma dos 2 números: "))
    except ValueError:
        continue
    if resposta == soma:
        print("Boa!")
        break
    else:
        print("Tente de novo.")
        continue
    


def main():
    while True:
        pergunta = str(input('Quer continuar? (S/N)\nSe quiser aumentar a dificuldade digite "D" e "C" para limpar a tela ou "m" para operações de menos. \n')).lower()
        if pergunta == "s":
                repetir()
                continue
                
        elif pergunta == "n":
                arq = open("Dados do jogo.txt", "a")
                arq.write(f""" • Pontuação: {pontuacao}\n""")
                arq.close()
                
                sys.exit(f"Tchau! Pontuação final: {pontuacao}")
                
        elif pergunta == "d":
                while True:
                    print("MODO HARD ATIVADO!")
                    pergunta_dura = str(input('O modo hard tem as mesmas instruções do normal: pressione "s" para continuar, "c" para limpar a tela e "f" para sair do modo hard.\n')).lower()
                    
                    if pergunta_dura == 's':
                        repetir_hard()
                        
                    elif pergunta_dura == 'c':
                        os.system(f"Pontuação: {pontuacao}")
                    elif pergunta_dura == 'f':
                        print("Desativando o modo hard!")
                        time.sleep(1.5)
                        os.system("clear")
                        break
                
        elif pergunta == "c":
                os.system("clear")
                
        elif pergunta == "m":
                menos()
        
        
        
 
 
 
def repetir():
    global pontuacao
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    soma = num3 + num4
    print(f"{num3} + {num4}?")
    
    while True:
        try:
            resposta = int(input("Digite a soma dos 2 números: "))
        except ValueError:
            continue
        if resposta == soma:
            print("Boa!")
            pontuacao += 20
            break
        else:
            print("tente de novo!")
            pontuacao -= 5
            continue

def repetir_hard():
        global pontuacao
        num5 = random.randint(100, 1000)
        num6 = random.randint(100, 1000)
        soma = num5 + num6
        
        print(f"Quanto é {num5} + {num6}?")
        
        while True:
            try:
                pergunta_3 = int(input("Digite a soma entre os números: "))
            
            except ValueError:
                continue
                
            if pergunta_3 == soma:
                print("Boa!")
                pontuacao += 50
                break
                
            else:
                print("Tente de novo!")
                pontuacao -= 15
                continue
        
    
def menos():
    global pontuacao
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    subtracao = num1 - num2
    
    print(f"{num1} - {num2} = ?")
    
    while True:
        try:
            tentar_sub = int(input("Digite o valor da subtração entre os 2 números: "))
        except ValueError:
            continue
        if tentar_sub != subtracao:
            print("Tente de novo!")
            pontuacao -= 1
        else:
            print("Boa!")
            pontuacao += 25
            break
    
if __name__ == "__main__":
    main()

    