import time
import random
import cowsay
import sys
import threading 

estado = {
"vacas mortas": 0,
"barulho": 0,
}
tempo_restante = True


# print(estado["atirar"]) ← Exemplo de como usar um dicionário 

def main():
    #capitulo_1("Devorado por um dino")
    
    time.sleep(2.5)
    
    #capitulo_2("Shhh!")
    
    #time.sleep(5)
    
    capitulo_3("A matança")
    
  
    
def capitulo_1(titulo):
    pensamento = 0
    print(f"Capítulo 1: {titulo}")
    print("Você foi devorado por um Dino no último jogo, você ainda está vivo, mas dentro dele...o que vai fazer??")
    
    while pensamento != 100:
        hmm = input("")
        pensamento += 1
            
        print(f"Pensamento em {pensamento}%")
        
    print("pensando...")
    time.sleep(3)
        
    print("Você lembrou que dinossauros não existem na vida real, e mesmo se existissem, eles devorariam as vacas, você fala isso em voz alta.")
    
    time.sleep(5)
    
    cowsay.trex("Huhh...desculpa humano!")
    
    time.sleep(2)
    
    print("*Dino some e você está em um lugar escuro, parece ser um porão, mas é tão escuro que você suspeita de estar fazendo parte de um ritual indiano...*")
    
def fala_cap_2():
    
    print('*Você sem querer acende uma lâmpada, você se depara com uma sala vazia sem nada, mas tem uma cadeira e um duto de ar, você fala: "JÁ SEI"!')
           
    time.sleep(9)
           
    print("Henry stickman: Eu também")
    
    time.sleep(0.001)
           
    print("""Você: AAAAA
então você usa a cadeira para alcançar o duto de ar, você começa a andar nas ventilações até escutar algumas vozes...""")
    time.sleep(8)

    print("Garibaldino: Agora com os nossos poderes bovinos, podemos colocar TANTA gordura na nossa carne que qualquer carne que alguém comer...vai causar ENTUPIMENTO NAS ARTÉRIAS!! E isso é só nossa primeira pesquisa de mutação genética... depois podemos dominar o mundo aos poucos com a nossa flatulência e causar aquecimento global!! >:)")
 
    time.sleep(18)
           
    print("""Você: OH MY GAH! EU PRECISO SALVAR O MUNDO...
*Você anda na ventilação até uma sala vazia, você sai do duto e há uma arma*
Você: Oh hohoho!!""")
    
    
def capitulo_2(titulo):
    print(f"capítulo 2: {titulo}")
    
    print("Você tem que escapar daqui, mas com o mínimo que consegue ver, tem duas portas: A e B, qual escolhe?")
    
    while True:
        escolha = str(input("Qual porta deseja escolher?\n")).lower()
        
        if escolha == "a":
            print("Você abre a porta...ela é bem velha e faz um barulho irritante.")
            
            estado["barulho"] += 30
            
            print("Mesmo assim você continua andando nos corredores. . .")
            
            estado["barulho"] += 25
            
            time.sleep(10)
            
            
        elif escolha == "b":
            
            print("A porta que abriu é bem moderna, não se sabe como vacas conseguem isso :/")
            
            estado["barulho"] += 5
            
            print("Mesmo assim você continua andando nos corredores. . .")
            
            estado["barulho"] += 25
            
            time.sleep(10)
            
        else:
            sys.exit("I-N-D-E-C-I-S-O, toma um game over aí para variar :>") #Anti bug em ação! :D
        
        if estado["barulho"] > 50:
            for _ in range(9999):
                cowsay.cow("VOCÊ FEZ BARULHO DEMAIS.")
            sys.exit("Final idiota.") # Juro que esse é o último sys.exit solto :)
            
        if estado["barulho"] < 50:
           
           fala_cap_2()
           
           
           break 
           
    
def falas_cap_3():
    print("""*Você pega A ARMA com brilho nos olhos*
    
arma: Com grandes poderes...

Você: Vem muita carne de vaca! 

Arma: BRUH...QUEEE???

Você: Que foi?

Arma: Isso é ridículo vey

Você: Tu é minha arma, me respeita ou vai ficar de castigo (nesse caso seria ficar sem bala)

Arma: ...

Você: PERA, TU FALA?!

Arma: Não.

Você: Okay...tenho algumas vacas para cozinhar... =)""")
def tempo():
        global tempo_restante
        time.sleep(50)
        tempo_restante = False
            
        
    
    
def contagem_reg():
    print("Começa em 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("COMEÇA!!")

def minigame(pontos):
    vida = 100
    t = threading.Thread(target=tempo)


    print('Bem vindo ao "minigame", eu falo com aspas porque...esse tal "minigame" é você matar um monte de vacas, as regras são simples...')
    
    time.sleep(5)
    
    print('Digita "K" para atirar em uma vaca, e só...boa sorte!!!')
    
    time.sleep(3.5)
    
    contagem_reg()
    t.start()
    
    while tempo_restante == True:
        time.sleep(1.5)
        rng = random.randint(1, 1000)
        if rng > 500 and rng < 670:
            cowsay.cow("MUHHH!")
            while True:
                atira = str(input("ATIRA!!\n")).lower()
               
                if atira == "k":
                    print("Boa!!")
                    print(f"Vida atual: {vida}")
                    pontos += 1
                    break
                else:
                    print("Perdeu vida!!")
                    vida -= 30
                    print(f"Vida restante: {vida}")
                    break
                if vida < 1:
                    final_

    return pontos
                
                  
             
def final_ruim():
    print("Com a sua RNG horrível ou sua capacidade de ter -200 de QI, você infelizmente não consegue matar a quantidade de vacas necessária para enfrentar o Garibaldino...")
    time.sleep(6.5)
    print("Após matar poucas vacas, você sai alegre cantarolando achando que arrasou, mas quando vê...um monte de vacas te cercam...")
    time.sleep(7.25)    
    for vacas in range(50): #Esse "vacas" é zoeira mesmo :>
        cowsay.cow("VOCÊ NÃO PODE ESCAPAR DA GENTE!!! MUHHH!")
    print('"Espera..." Escuta se outra voz no fundo')
    print("Você: Huh...? Quem é tu??!")
    print("Garibaldino: Eu sou o líder das vacas...HEHEHEH... Você foi BEM impressionante ao chegar aqui, eu acho")
        

                
                
           
def capitulo_3(titulo):
    
    print(f"Capítulo 3: {titulo}")
    
   # time.sleep(5)
    
    falas_cap_3()
    
   # time.sleep(15)
    
    minigame_cap_3 = minigame(estado["vacas mortas"])
    print(f"pontuação: {minigame_cap_3} vacas mortas.")
    
    time.sleep(2.5)
    
    if minigame_cap_3 <= 4:
        print('Bruh')
    
    
    
    
          
main()