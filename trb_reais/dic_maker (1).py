import sys
lista = []
def main():
    
    dic()

def dic():
    
    while True:
        
        new = str(input("Você quer criar um novo dicionário?(S ou N)\n")).lower()
        
        if new == "s":
            global dicionario
            dicionario = {}
            nome = str(input("Nome do primeiro dicionário: "))
            
            if nome:
                
                
                print(nome)
                
                info = (input("Adicione uma informação: "))
                
                if info:
                    dicionario[nome] = info
                    lista.append(dicionario)
                    print(nome)
                    print(dicionario)
                    return dicionario
                    
        if new == "n":                                       
            break
            
        else:
            break
                                                                                                                                
def ver():
  
    for dics in lista:
       
        print(dics)
        
if __name__ == "__main__":
    main()
    
    