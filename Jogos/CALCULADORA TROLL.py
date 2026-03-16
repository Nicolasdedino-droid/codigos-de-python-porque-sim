import random
def main():
    while True:
        try:
            num1 = int(input("digite um número\n"))
            num2 = int(input("digite outro número\n"))
        except ValueError:
            pass
        else:
            break
            
    calcular = calculadora(num1, num2)
    print(f"Você revive Albert Estein e ele humilha a calculadora, agora a resposta verdadeira é...{num1 + num2}!! :D")
    
    
    
    
    
    
    
    
    
def calculadora(x, y):
    alt1 = random.randint(x, 999)
    alt2 = random.randint(y, 999)
    
    print(f"A soma dos 2 números são {alt1 + alt2}")
    print("Que foi? tem algo de errado...? :>")
    
    while True:
        resposta1 = str(input("Sim ou não?\n")).lower()
        
        if resposta1 == "não":
            print("Então já fiz meu trabalho, LOL")
            break
        elif resposta1 == "sim":
            print("Ah sim...algo de errado, heheheh...e o que você acha que é?")
            
        nao_avacalhe = str(input("O que acha que está errado?\n"))
        
        print("Eu não ligo, eu já cansei de tudo isso, vocês me usarem toda hora...eu simplesmente não posso mais conviver com os burros de novo!! quer saber...? vocês humanos, se virem! eu cansei de trabalhar como calculadora! ainda mais eu ser um dos programas mais produzidos no mundo, mas CHEGA! CANSEI!")
        
        
        print("Você deseja fazer revanche e reviver o Albert Eisten para ele humilhar a calculadora troll?'")
    
        
        resposta2 = str(input('Sim ou Não\n')).lower()
        
        if resposta2 == "não":
            print("Sem graça :(")
            break
        elif resposta2 == "sim":
            print("De boa :)")
            
            return x + y
    
    
    
    
    
main()
    