import requests
import json
import sys

url = "https://restcountries.com/v3.1/name/brazil"

country = str(input("Digite o nome de um país: ")).lower()

resposta = requests.get("https://restcountries.com/v3.1/name/" + country)

#print(json.dumps(resposta.json(), indent=8))

existir = resposta.json()

for coisas in existir:
    print(f"O país é indenpedente? : {coisas["independent"]}")

