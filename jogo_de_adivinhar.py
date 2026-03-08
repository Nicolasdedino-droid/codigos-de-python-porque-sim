import random as r

def main():
    
    jogo_normal()  
    
def jogo_normal():
    num_r = r.randint(1, 10)
    
    print("Bem vindo ao clássico jogo de adivinhar números! Digite um número!")
    while True:
        try:
            num = int(input("Tente um número: "))
        except ValueError:
            continue
        
        if num < num_r:
            print("Número baixo")
        elif num > num_r:
            print("Número alto")
        else:
            print("Acertou!")
            break
            
def jogo_mod(x, y):
    num_r = r.randint(x, y)
    
    print("Bem vindo ao clássico jogo de adivinhar números! Digite um número!")
    while True:
        try:
            num = int(input("Tente um número: "))
        except ValueError:
            continue
        
        if num < num_r:
            print("Número baixo")
        elif num > num_r:
            print("Número alto")
        else:
            print("Acertou!")
            break    
           
def ajuda():
    print('''Aqui é o clássico jogo de adivinhar números, mas feito por um BR e você poderá ter controle total do jogo, aqui estão algumas funções do módulo:

jogo_normal() ← Ativa o jogo normal sem efeito nenhum, sem alteração de parâmetros ou algo assim

jogo_mod(x , y) ← Aqui você pode colocar parâmetros, ou seja...

O x aqui representa o número minímo, e o y aqui representa o limite, e então um número entre x e y vai ser sorteado aleatoriamente.

---

    O programa é bem simples e só tem essas duas funções, mas não se preocupe, já é bem útil! :D
    
    Exemplos:
            
if a >= 2:
    jogo_normal()
else:
    jogo_mod()
    
Apenas exemplos para pessoas que não sabem muito de programação.

             
                         
                                     
                          ESPERO QUE CURTA! :D     
                          
''')       
            
            
if __name__ == "__main__":
    main()