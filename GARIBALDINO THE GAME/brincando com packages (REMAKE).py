import cowsay
import sys
import time
import os

print("AVISO: Este programa pode ser ofensivo para haters do Games Edu, usuários do (antigo) Twiter e para os fãs da Emily Vicky (Isso já fica claro se eu errar o nome desses manos, eheh...)")

time.sleep(8.5)

def main():
    
    dialogo(0.05, "Isto é um remake do primeiro programa do Garibaldino! Espero que aproveite :> (mesmo se isso durar menos que a paciência de um Italiano irritado por causa de um ketchup na Pizza.)\n")
    time.sleep(2.5), os.system('clear')
    
    dialogo(0.07, '''VISUAL NOVEL SEM SENTIDO REMAKE! 
    
Responda apenas "sim" ou "não", e SEM...Eu repito, SEM abreviar essas palavras que já são curtas! >:(

''')

    while True:
        pergunta = str(input('Você gosta de carne? ')).lower()
        
        if pergunta == "sim":
            pessima_escolha()
            
        elif pergunta == "não":
            
            voce_estragou_tudo_DENOVO_porque_voce_tem_que_falar_sim_ao_em_vez_do_não()
        elif pergunta == "s":
            dialogo(3, "P-R-E-G-U-I-Ç-O-S-O") 
            break
        elif pergunta == "n":
            dialogo(10, "Espera só até o final...MUAHHAAHHAHAHAAHAHAHAH! NADA!!")
            break
        else:
            sys.exit("-_-")
 
    
    

def dialogo(tempo, texto):
   
     for palavras in texto:
         sys.stdout.write(palavras), time.sleep(tempo)
         sys.stdout.flush()
        
def pessima_escolha():
    cowsay.cow("MUHH! VOCÊ OFENDEU A SOBERANIA MIMOSA!")
    
    uhhhh = input("O QUE TU FEZ RAPAZ?!\n")
    
    for vacas in range(50000):
        cowsay.cow("MUHHHHHHHHHHHH!")
        
            
    sys.exit("Final ruim...")    
  
  
def voce_estragou_tudo_DENOVO_porque_voce_tem_que_falar_sim_ao_em_vez_do_não():
    sys.exit("NÃO EXISTE FINAL FELIZ NESSA VERSÃO!!!!")
    
if __name__ == "__main__":
    main()
