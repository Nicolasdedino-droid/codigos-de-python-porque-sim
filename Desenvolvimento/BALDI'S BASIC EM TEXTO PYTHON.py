import random
import sys

print("Você se lembra de Baldi's Basic In Education and Learning? Isso é uma simulação em texto!")

def main():
    caderno_1 = caderno()
    caderno_2 = caderno()
    
    
    
    
    
    
    
    
    
    
    
def caderno():
    
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    simbolo = random.choices("+", "-")
    
    primeira_pergunta = num1 + num2
    segunda_pergunta = (num1 - 2) - (num2 + 3)
    terceira_pergunta = (num1 * 2)  +  (num2 - 1)
    
    print(f"Quanto é {num1} + {num2}?")
    
    while True:
        try:
                resposta = int(input("Resultado: "))
            
        except ValueError:
            sys.exit("VOCÊ REALMENTE SE ACHA INTELIGENTE POR ISSO?!")
            
        if resposta == primeira_pergunta:
            print("Acertou!")
            print(f"Quanto é {num1 - 2} - {num2 + 3}?")
            
    
        elif resposta == segunda_pergunta:
            print("Acertou!")
            print(f"Quanto é {num1 * 2} + {num2 - 1}?")
            
        elif resposta == terceira_pergunta:
            print("Meus parabéns! você é muito incrível!")
            
        else:
            print("ERROU")
            
    
        
        
        
        
        
        
        
        
        
main()
    