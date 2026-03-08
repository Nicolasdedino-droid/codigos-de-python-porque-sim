import cowsay
import sys

def main():
    print("DLC do jogo {sem_titulo}...QUEM FOI A MULA QUE ESQUECEU DE COLOCAR O F PARA FORMAT-")
    print("Comandos: sim ou não, nada mais.")
    
    while True:
        entendeu = str(input("Entendeu?\n")).lower()
        
        if entendeu == "nini":
            print("""créditos: eu
            música: eu
                               python: eu
                                                  barra de espaço: EU
                                                       eu: EU
                                                       
                                                       
                                                       Thank you for playing! 
                                              Obrigado 929929 ifs por fazer meu código rodar! :D""")
                                              
            sys.exit()
        
        elif entendeu:
            print("Após você ser sequestrado pela as vacas por gostar de carne, uma aproxima de você...")
            cowsay.cow("Você finalmente acordou, huh? Olha só...você vai ser sacrificado pelo nome das vacas por você gostar de comer a nossa carne, mas como que sou bonzinho, eu vou te dar o direito de ligar para a sua mãe :)")
            
            ligar = str(input("Ligar pra ela?\n")).lower()
            
            if ligar == "sim":
                print("...Ninguém responde")
                cowsay.cow("Ah...esqueci que você não tem mãe, LOL!!!!! Agora você será sacrificado...")
                
                escolha = str(input('Escolha a sua morte: Digite "d" para morrer pra um dinossauro ou digite "d" para morrer pro dinossauro.\n')).upper()
                
                if escolha == "D":
                    for _ in range(999):
                        cowsay.trex("RAAAHHH!")
                        
                    sys.exit("Final ruim 2/2")
                else:
                    print('Oh my gah! você antes de ser devorado por um dino, viu um código secreto: "123"')
                    sys.exit("Final ruim 1/2")
                    
                    
            elif ligar == "não":
                cowsay.cow("Você nem se importa com a sua mãe? que triste. :(")
                sys.exit("Final triste")
                
            elif ligar == "123":
                cowsay.cow("OH NÃO, VOCÊ LIGOU PRO MCDONALD! AAAAAAAAAAAAA-")
                sys.exit('Final indefinido: agora digita "nini" no início')
                
            
            
            
            
            
            
            
            
            
            
main()
    
    
    
    
    
    
    
    
    