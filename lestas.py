nomes = ["João", "Mateus" ,"Maria"]
print("João morrerá...")
print(f"o {nomes.pop(0)} morreu ;(")
print(f"Lista atual: {nomes}")
name = input("Adicione um nome pra lista :>\n")
nomes.append(name)
print(f"Nomes atuais: {nomes}")