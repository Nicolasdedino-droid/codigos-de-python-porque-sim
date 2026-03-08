import random

nomes = ["jojon", "Maria Braga", "Jejum dos Jins", "Joao calvanereiro", "AHAHAH", ":(", "nekolas", "Oi tim é uma companinha seu aninal", "idk", "João boaPart3", "Nicolax", "Insanity", "Help", "CADE A LORE DE FNAF?!", "Hehehe HAW", "Sansta", "last stand", "Loyality studios", "CHICKEY JOCKEY!", "Rythm HELL YEAHHHHHH", "Muahahahahahahahhahahahahahahahahaahahahaahahaah", ":/", "emoticon", "vs", "microsoft", ":0"]
random.shuffle(nomes)

print(nomes)
print("qual dos nomes é alguém real?")

while True:
    resposta = input("digite aqui: ")
    if resposta == "Maria Braga":
        print("parabéns!")
        break