azule = '\033[96m'

texto1 ='''Hatsune Miku: Olá! Eu sou a Hatsune Miku, uma idólo digital! Se quiser saber mais sobre, digita "ajuda()"

Mas de qualquer jeito, saiba que eu sou a sua assistente nesse caso, e NÃO me pergunte como eu estou no Python~...

Heheh, zoeira, mas TODAS as instruções estão no ajuda(), digita isso e sua vida será fácil para eu e para você! :D'''

texto_help ='''Este aqui é um programa que você pode usar a Hatsune Miku como asssistente, onde há diversas opções variadas e divertidas, com certeza não é um programa necessário, MAS...É aquela coisa, ajuda de uma forma divertida no seu Python, principalmente para descontrair, então não é de todo mal! :D

---

    INSTRUÇÕES:
        
        Digite "Miku.call()" para chamar a Miku como assistente real, ela vai aparecer e vai te fazer uma pergunta, onde você estará livre para digitar algum comando, e dependendo do comando, ela vai fazer para você e o programa vai ACABAR na hora, então se quiser falar com ela várias vezes aí, prepare seu For e While!!
        
        
---
    
    COMANDOS:
        
        Digitar "math" faz ela fazer contas matemáticas do jeito que quiser...Apenas não tente sobrecarregar ela. . . :>
        
        Digitar "music" faz ela te exibir uma série de músicas só dela
        
        Digitar "Kasane Teto" faz ela- [RESTRIGIDO]
        
        Digitar "python" faz ela te dar alguma dica aleatória de Python
        
        Digitar "talk" faz ela falar alguma coisa aleatória
        
---

É ISSO! O programa ainda está em Beta mesmo, mas nada que seja ruim, é apenas feito por um pré adolescente que quer se divertir! ;)

Então espero que curta isso, caso contrário...RETRY NOW!!

                            Eu gosto de ti! ;D
                                    
'''

texto2 = "Oie!! Estou pronta para receber alguma instrução! :3"

texto3 = "Matemática?! estou pronta para responder algumas perguntas matemáticas..."

despedida = """Olha...eu tenho mais coisas para fazer na vida! >:(
Tchau."""

#---
#PROIBIDO MEXER NESTA ÁREA!
#---


#--- SEPARAÇÃO ENTRE TEXTO E FUNÇÕES---


def main():
    
 
    Miku()
    
    
def Miku():
   #Aqui gera a fala da Hatsune Miku após iniciar o programa.
    print(azule,texto1) 
    
#===Separando função===
    
 
def ajuda():
    #Help básico versão abrasileirada.
    print(texto_help)
    
#---~Separando funções outra vez~---
    
def call():
    #Apresentação dela
    print(azule,texto2)
    
    while True:
        inst = str(input("Digite algum comando: ")).lower()
        
        if inst == "math":
            print(azule,texto3)
            break
        else:
            print(azule, despedida)
            break
            
            
    
    
if __name__ == "__main__":
    main()
   
    
