import cowsay
import sys
import random
import statistics 
import time

print("Prequel: COWSAY, A REVOLTA DAS VACAS")

print("""Olá, eu sou o Garibaldino, e eu sou uma vaca muito Mimosa :3
Hoje vou te contar como eu virei a líder das vacas supremas, e vou dar detalhes de como eu torturo pessoas que NÃO são vegetariana. :D""")

time.sleep(5)


def main():
    capitulo_1()
    
    time.sleep(7)
    
    prova_resultado = prova()
    print(f"Você gabaritou na prova, a média da escola é {prova_resultado}, tu passou de ano rapaz! mas...o Mateus NÃO...")
    
    time.sleep(2)
    
    revanche_mateus()
    
   
def capitulo_1():
    capítulo_1 = """                                                            
 ,-----.                 ,--.          ,--.            ,--. 
'  .--./ ,--,--. ,---. ,-'  '-.,--.,--.|  | ,---.     /   | 
|  |    ' ,-.  || .-. |'-.  .-'|  ||  ||  || .-. |    `|  | 
'  '--'\\ '-'  || '-' '  |  |  '  ''  '|  |' '-' '     |  | 
 `-----' `--`--'|  |-'   `--'   `----' `--' `---'      `--' 
                `--'                                        """
                
    print(capítulo_1)
    
    print("""Garibaldino: Oi Mateus! como vai aí?
    
Mateus: Nada bem...mataram a minha mãe para fazer McDonald's dela, e também não estudei para a prova de hoje:(

Garibaldino: O-OQUE?! VOCÊ....VOCÊ NÃO ESTUDOU PARA A PROVA?!

Mateus: QUE?! VOCÊ LIGA MAIS PARA A PROVA DO QUE A MINHA MÃE?

Garibaldino: Quer dizer, ela tinha uma cara deliciosa na grelha, como qu-

Mateus: ...CHEGA! NÃO SOU MAIS SEU AMIGO!

Garibaldino: N-não! calma, eu poss-

*Mateus sai*

Garibaldino: Droga...CULPA DOS HUMANOS POR EU FALAR ISSO! >:(""")
   
   
def prova():
    print("Hora da prova.. ")
    numeros = 100, 500, 200
    media = statistics.mean(numeros)
    
    pergunta_troll_1 = random.randint(100, 10000)
    pergunta_troll_2 = random.randint(100, 10000)
    resposta_maldita = pergunta_troll_1 * pergunta_troll_2
    
    print(f"Quanto é {pergunta_troll_1} vezes {pergunta_troll_2}?")
    
    while True:
        try:
            tente_LOL = int(input("Digite aí e se ferre XD\n"))
        except ValueError:
            continue
        if tente_LOL == resposta_maldita:
            print("Boa!")
            return media
        else:
            sys.exit("Calculadora: EU NÃO EXISTO?! (Sim, estou sendo cruel nessa parte) XD")
            
            
            
def revanche_mateus():
   print("Mateus: Garibaldino... VOCÊ ME CAUSA INVEJA! CHEGA DESSAS BOSTAS! EU QUERO QUE FAÇA UMA ESCOLHA...apertando o botão A, você vai salvar a sua mãe, o botão B, vai salvar seu pai...")
   
   cowsay.cow("FILHO! ME SALVA!")
   cowsay.cow("É VEY, SALVA NOIS AÍ")
   
   print("Garibaldino: Nem sei quem é o pai e a mãe XD")
   
   time.sleep(5)
   
   while True:
       escolhe = str(input("Escolha sabiamente...\n")).lower()
       
       if escolhe == "b":
           sys.exit("Os 2 morrem ")
       if escolhe == "a":
           sys.exit("Os 2 viram McDonalds")
       else:
           print("(Essa é a decisão canônica que transforma os dois outros jogos do cowsay em realidade...)")
           sys.exit("Garibaldino: NÃO...EU... Mateus, me perdoe por todos meus pecados...a partir de agora, eu vou sacrificar humanos que comem vacas!!")
   
    
main()