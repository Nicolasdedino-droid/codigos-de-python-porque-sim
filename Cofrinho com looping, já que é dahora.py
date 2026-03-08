def main():
	valor = int(input("digite um valor:\n"))
	piggy_bank_balance(valor)
	
	
	
	
def piggy_bank_balance(num):
	contador = 0
	for i in range(num):
		print(f"{num} R$")
		num -= 500
		contador += 1
		if num == 0:
			print(f"a compra chegou ao fim! sobrou {num} R$, onde comprou {contador} vezes para chegar a zero!")
			break
		elif num > 1000000:
			print("valor muito alto")
			break
			
		
		
		
main()