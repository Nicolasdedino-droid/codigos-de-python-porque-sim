import webbrowser
import time

print("( ͡° ͜ʖ ͡°)")

while True:
    nome = input("Digite seu nome: ").strip()
    idade = input("Digite a sua idade: ").strip()
    
    if nome == '' or idade == '':
        continue
    else:
        break
    
print(f'Olá, {nome}, você verá como estão os projetos em andamento...Mas apenas digite "Q"')

que = input('Digite "q": ').upper()

if que == "Q":
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXc" + que)
else:
    for _ in range(10000):
        print('DIGITE "Q"!!!')
        
DIGITA = input(">>>").upper()

if DIGITA != "Q":
    webbrowser.open("https://youtu.be/wcinzmfZeCc?si=Di5ALLZUttNMGFhZ")
    
else:
    print("HAHAHAH...SABIA QUE VOCÊ FOI RICK ROLL?!")
    time.sleep(0.75)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    

