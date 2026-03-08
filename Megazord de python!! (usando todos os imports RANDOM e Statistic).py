import random #escopo global
def main():
    
    resultado_escolha = escolha() #jogo do cara ou coroa
    print(f"o lado é {resultado_escolha}")
    
    adivinhar = adivinhacao() #o famoso joguinho de adivinhar o número
    print(adivinhar)
    
    resultado_baralho = embaralhar() #ao menos consegui uma utilidade criativa para esse conteúdo, heheh...
    print(f"o nome era {resultado_baralho}")
    
    
    
    
    
    
    
    
def escolha():
    lados = random.choice(["Cara", "Coroa"]) #escolha de lados
    
    tentativa = str(input("qual lado vai cair? cara ou coroa?\n")).capitalize() #usuário tenta...
        
    #séries de condicionais sobre True e False...
    if tentativa == lados:
        print("Acertou!")
    else:
        print("Errou...")
            
    return lados
    
    
    
def adivinhacao():
    limite = 10 #Aumentar o limite fica aqui!
    num = random.randint(1, limite)
    print("tente adivinhar o número! de 1 à 10") 
    
    while True: #Looping infinito atè o usuário acertar
        try: #Evitar erros...
            tentar = int(input("digite um valor: "))
        except ValueError:
            continue #Continuar o looping
        
        if tentar > num: 
            print("número alto")
        elif tentar < num:
            print("número baixo")
        else:
            print("acertou!")
            break
            
    return f"o número secreto era {num}"
    
    
def embaralhar():
       
       nomes = ["Yummy!", "Noooo, la polizia", "mascote samsung muahahah", "fortnite or PUBEGE?!", "Crt", "Bob glob", "Levan Pollka", "Ritmo orientando a carengueijo", "brainfu##", "SYSTEM SHUTDOWN!", "Eu quero café :/", "Sim, eu amo queimar amazônia (uma nota da França)", "pai, quando eu crescer, vou ser britânico e fazer um museum, muahhsahsh!", "Mariana grande", "Poop Marley", "WHUTHUUUUUU HELLLL", "Muito engraçado essa história do |}{€[¥{€×€{¢]¢[¢[¢{¢{", "Meu deus, essa lista é muito desorganizado, eu esqueci de usar 3 aspas, LOL", "mensagem secreta...quer dizer, nem tanto assim", "Eu sou chinês...EU COMO CACHORRO...Quente, heheh", "MEUS DEDOS ESTÃO DOENDO!!", "...", "Hatsune Miku miku miku miku beam?", "potato knishes", "Entropia ou singularidade?", "A"] #Oh my god...what i have done? heheh...
       
       random.shuffle(nomes) #embaralha aleatoriamente a lista anterior
       
       print("quais palavras dessa lista é um nome real?")
       
       print(nomes)
       
       while True: #Looping que só sai quando o usuário acerta um nome que existe
           boa_sorte = str(input("Digite o nome: ")).strip().capitalize()
           
           if boa_sorte == "Mariana grande":
               print("certou mizerave!!")
               
               return boa_sorte
           
           
       
    
    
    
    
    
main() #Oi! eu sou o main e gosto de ficar sozinho no código dos outros! eu muito bem poderia sofrer bullying, mas eu que trabalho com o def main, meu melhor amigo, sem mim, esse código não ia ter valor! XD