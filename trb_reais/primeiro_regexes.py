import re

valor = input("Digite um valor e algum sinal identificador de moeda: ")

if re.search(r'^\d+\$$', valor):
    print("Legal")
else:
    print('Ilegal!')