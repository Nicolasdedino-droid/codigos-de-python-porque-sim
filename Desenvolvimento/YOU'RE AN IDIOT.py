# RECRIANDO "You're and idiot"
import sys
sys.path.append("/storage/emulated/0/Python/módulos")
from diálogo import dialogo

explicar = '''O famoso "vírus" you're an idiot era um Malware que funcionava da seguinte maneira:
    
    Quando você entrava em um site suspeito, aparecia um botão falando que quer ser clicado.
    Ao clicar, você perdia o controle do seu navegador e a sua janela começava a se mexer enquanto tocava uma animação e um som que te chamava de idiota.
    Era algo irritante, já que, se você tentasse sair, a janela ia ser duplicada, e isso ocorria até o seu computador travar.
    O autor do vírus e anônimo e não se sabe quem criou, mas ele está disponível em um site específico que não vou lembrar :^
    porém como que aquele malware era propositalmente irritante, as pessoas aceitaram a zoeira e existe até mesmo clipes sobre.
    Ao executar o meu programa com a entrada, eu irei recriar isso, mas só funciona no celular! Porque eu estou fazendo isso no celular.'''
    
    

#--- SEPARAÇÃO ENTRE MÓDULOS E A PARTE EXECUTIVA---

dialogo(0.04, '''Este programa é uma recriação do famoso "You're an idiot".

Para rodar o programa, digite "idt" e dá enter.

Para saber o que é "You're an idiot" digite "help" e dá enter.''')

while True:
    entrada = input(">>> ").lower()
    
    if entrada == "idt":
        print("You're an idiot...")
    elif entrada == "help":
        dialogo(0.04, explicar)

