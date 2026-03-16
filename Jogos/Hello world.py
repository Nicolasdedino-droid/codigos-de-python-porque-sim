import random
import sys
import time
import os
sys.path.append("/storage/emulated/0/Python/módulos")
from diálogo import dialogo

def main():
    
    HWMDP()
    
    
#HWMDP é uma abreviação para "hello world mais dificil no Python"    
def HWMDP():
    jogo = ["cara", "coroa"]
    dialogo(0.02, "A sua tela não está estática, esse é um jogo de RNG, apenas espere! :>")
    while True:
        num = random.randint(1, 100)
        time.sleep(0.05)
        
        if num > 99:
          
            dialogo(0.03, """Você passou da primeira etapa! O RNG...
     
Agora esse é um jogo de cara ou coroa, ou seja, é 50% de chance de perder ou 50% de chance de ganhar... XD

está pronto?""")

            ready = str(input("Pronto? (S/N)\n")).lower()
            if ready == "s":
                escolher = random.choice(jogo)
                
                dialogo(0.05, "Tirando um resultado...por favor, aguarde.")
                
                time.sleep(5)
                
                os.system('cls' if os.name == "nt" 'cls' else 'clear')
                
                print(f"Você tirou {escolher}")
                
                dialogo(0.04, "Agora vamos fazer o jogo de 50/50!! Heheheh...Espere para obter a surpresa.")
                
                time.sleep(4)
                
            
                if escolher == "cara":
                    sys.exit("Perdeu, tirar cara aqui é perder! XD")
                elif escolher == "coroa":
                    dialogo(0.05, 'Ganhou...! Mas só por causa disso, você acha que tem o direito de obter aquele icônico "Hello world"? ...ESPERA, EU FALEI JUSTAMENTE ISS-')
                    print("Hello World!")
                    break
            elif ready == "n":
                sys.exit("Sem graça...")
    
if __name__ == "__main__":
    main()