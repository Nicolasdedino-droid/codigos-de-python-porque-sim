import random

num = random.randint(1, 10)

print("adivinhe o número de 1 à 10!")

while True:
    try:
        tente = int(input("digite um número: "))
    except ValueError:
        print("Valor digitado não é um número")
        continue
    if tente < num:
        print("número baixo")
    elif tente > num:
        print("número alto")
    elif tente == num:
        print("você ganhou!")
        break