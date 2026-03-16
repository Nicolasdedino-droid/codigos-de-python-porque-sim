import statistics as st

def main():
   
    print(media())
    
  
def media():
    lista = []
    while True:
        try:
            NUMs = int(input("Digite um número para indicar a quantidade de números que quer digitar: "))
            for _ in range(NUMs):
                numeros = int(input("Digite os valores\n"))
                lista.append(numeros)
        except ValueError:
                continue
        else:
                break

    return st.mean(lista)
                
if __name__ == "__main__":
    main()           