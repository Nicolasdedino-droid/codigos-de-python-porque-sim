nome = input("nome de usuário por favor\n")
senha = input("senha do usuário, por favor\n")
def acesso_legal(nome, senha):
	return (nome, senha)
acessar = acesso_legal(nome, senha)
if acessar == acesso_legal("admin", "1234"):
	print("acesso liberado")
elif acessar == acesso_legal("admin", senha):
	print("senha do usuário incorreta")
elif acessar == acesso_legal(nome, "1234"):
	print("nome do usuário errado")
else:
	print("senha e nome errados")
