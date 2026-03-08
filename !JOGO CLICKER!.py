import sys
def main():
    dinheiro = 0
    click = 1
    upgrades = {"Upgrade1": 50,
    
    "Upgrade2": 1000,
    "Upgrade3": 25000,
    "Upgrade4": 100000,
    "Upgrade5": 250000,
    "Upgrade6": 500000,
    "Upgrade7": 5000000
    }
    
    
    print('''Bem-vindo ao meu jogo clicker
Enter = clicar, "p" para comprar upgrade e "q" para sair do jogo e "v" para ver a lista dos upgrades e seus custos''')

    while True:
        print(f"Dinheiro: {dinheiro} R$")
        inp = input(">>>").lower()
        
        dinheiro += click
        
        if inp == "v":
            print(upgrades)
            
        elif (inp == "p" and dinheiro >= 99999999999):
                print('Parabéns! você zerou o jogo, vou te passar um segredo: pressione "$$$&#" para desbloquear o modo desenvolvedor')
                dinheiro += dinheiro
                click += click
        
        elif (inp == "p" and dinheiro >= 5000000):
             click += dinheiro
             dinheiro -= dinheiro
             
        elif (inp == "p" and dinheiro >= 500000):
                 dinheiro -= 500000
                 click += 5000
             
        elif (inp == "p" and dinheiro >= 250000):
                dinheiro -= 250000
                click += 1000
         
        elif (inp == "p" and dinheiro >= 100000):
                dinheiro -= 100000
                click += 500
            
        elif (inp == "p" and dinheiro >= 25000):
                dinheiro -= 25000
                click += 250
            
        elif (inp == "p" and dinheiro >= 1000):
               dinheiro -= 1000
               click += 25
           
            
            
        elif (inp == "p" and dinheiro >= 50):
            dinheiro -= 50
            click += 1
            
        elif inp == "q":
            print("Saindo da experiência...")
            sys.exit()
            
           
        elif inp == "$$$&#":
            print("Modo desenvoledor ativado")
            
            try:
                coloque = int(input("Digite o dinheiro que deseja: "))
            except ValueError:
                pass
            
            else:
                dinheiro += coloque
                continue
            
            
            
 

main()