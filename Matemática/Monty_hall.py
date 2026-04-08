#Monty hall problem in Python

import random
import sys
sys.path.append('/storage/emulated/0/Python/Módulos')
from Tratar_erros import intinput
import time

def monty_choice(n_user, carro):
    while True:
        real_escolha = random.randint(1, 3)
        if real_escolha == n_user:
            continue
        elif real_escolha == carro:
            continue
        else:
            return real_escolha    

def sorteio(s_n, n_user, carro):
    if s_n == 's':
        print(f'Mudando para a porta restante....{carro} tu ganhou o carro!!')
        
    elif s_n == 'n':
        print(f'A porta permanece: {n_user}...Tu não ganhou o carro! :(')
        

print('''Olá cara parcitipante!

Você vai escolher uma das 3 portas, onde 2 portas podem ter um bode e a que restou pode ter um carro!
Seu objetivo é ter a sorte de ganhar o carro!

Mas uma coisa: Quando tu escolher a porta, você não verá a porta que escolheu, porque euzinho aqui vai abrir uma das portas para tu!! 

Depois disso eu irei lhe questionar se tu quer ficar com a porta que escolheu ou se quer mudar a sua escolha...

digite números entre 1 e 3 para escolher as portas!!

Boa sorte!˜
''')

escolher = intinput("Escolher: ")


if escolher > 3 or escolher < 1:
    sys.exit('No...Meu querido!! Tu leu minhas instruções?!')
    
else:
    print('Perfeito! Deixe-me abrir uma porta...')
    print('Aguardando resposta... ', end='', flush=True)
    
    while True:
        car = random.randint(1, 3)
        if car == escolher:
            continue
        else:
            break
        
    guardar_chc =monty_choice(escolher, car) 
    time.sleep(6)
    print(f'''Resposta concretizada!
    
Meu caro participante, a porta que abrirei é...{guardar_chc}!!

Tu quer mudar de porta?!''')

while True:
    mudança = input('Digite "s" para sim e "n" para negar: ').lower()
    
    if mudança == 's':
        sorteio(mudança, escolher, car)
        break
    elif mudança == 'n':
        sorteio(mudança, escolher, car)
        break
