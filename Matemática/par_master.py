def main():
   
    while True:
        try:
            num = int(input("Digite um número: "))
        except ValueError:
            continue
            
        exibir_div = par(num)
        
        print(f"A divisão entre o número e 2 é: {exibir_div}")
        
        escolha = input("Você quer continuar? (S/n)\n").lower()
        
        if escolha == "s":
            continue
        elif escolha == "n":
            break
        
   
   
   
   
def par(num):
        if num % 2 == 0:
            print("O número é par.")
            return num / 2
        else:
            print("O número é ímpar")
            return num / 2
            
            
if __name__ == "__main__":
    main()