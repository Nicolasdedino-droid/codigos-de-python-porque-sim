import cowsay
import sys
def main():
    
    print("VISUAL NOVEL SEM SENTIDO: Responda apenas sim ou não")
    while True:
        pergunta = str(input("Você gosta de carne?\n")).lower()
    
        if pergunta == "sim":
            pessima_escolha()
        elif pergunta == "não":
            uma_funcao_totalmente_inutil_nesse_caso_ja_que_isso_tudo_envolve_voce_falar_sim()
            
            
            
            
            
            
            
            
def pessima_escolha():
        cowsay.cow("VOCÊ SERÁ SACRIFICADO PELA AS MIMOSAS!!")
        
        ultima_esperanca = str(input("UUHHHHH...O QUE TU FEZ!?\n"))
        
        for _ in range(500):
            cowsay.cow("MUUUH!")
            
            
 
        sys.exit("Final ruim.")
            
def uma_funcao_totalmente_inutil_nesse_caso_ja_que_isso_tudo_envolve_voce_falar_sim():
            sys.exit('Eehhmm...acabou a história, lol, mas você vai sair do programa para ver o nome do final "bom", ou melhor, o nome da FUNÇÃO, heheheh.')
            
        
        
        
        
        
main()
        