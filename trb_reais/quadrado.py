def main():
  
    num = int(input("Digite um número: "))
   
            
    print(f"O valor quadrático do seu número é: {quadrado(num)}")
    
def quadrado(x):
    return x * x
    
if __name__ == "__main__":
    main()