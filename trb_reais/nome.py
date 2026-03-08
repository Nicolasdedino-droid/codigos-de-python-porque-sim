def main():
    nome = str(input("Nome: "))
    print(oi(nome))
    

def oi(para="mundo"):
    return f"Olá, {para}"
    
if __name__ == "__main__":
    main()