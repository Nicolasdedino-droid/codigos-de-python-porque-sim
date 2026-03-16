import random

moeda = random.choice(["cara", "coroa"])
while True:
    pergunta = str(input("vai cair cara ou coroa?\n"))
    
    if pergunta == "cara" or "Cara":
        print(f"o resultado é {moeda}")
        break
    elif pergunta == "coroa" or "Coroa":
        print(f"o resultado é {moeda}")
        break
    