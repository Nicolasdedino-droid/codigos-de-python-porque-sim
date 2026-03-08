def main():
	piggy_bank_balance(2500)
	
	
	
	
def piggy_bank_balance(num):
	contador = 0
	while num > 0:
			print(f"{num} R$")
			num -= 500
			contador += 1
			if num == 0:
				print(f"a compra chegou ao fim! sobrou {num} R$, onde comprou {contador} vezes para chegar a zero!")
				break
		
		
		
main()