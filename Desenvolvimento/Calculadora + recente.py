import math

def main():
    
    while True:
        try:
            num1 = int(input('Insira um valor: '))                        
        except ValueError:
            
            continue
            
        else:
            calculadora(num1)
    
   
    
def calculadora(n1):
    lista = []
    for _ in range(n1):
        try:
            valores = int(input('digite os valores: '))
            lista.append(valores)
        except ValueError:
            return 'Erro de valor.'
    
    
    operation = input('digite uma operaçao: ')
    match operation:
            case '+':
                print(sum(lista))
            case '-':
                for n in lista:
                    a = 0
                    a += 1
                    print(lista[0:a])         
            
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    