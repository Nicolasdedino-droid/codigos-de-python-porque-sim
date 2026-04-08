import sys
sys.path.append("/storage/emulated/0/Python/Módulos")
from Tratar_erros import intinput

def main():
    num1 = intinput("Digite um valor: ")
    num2 = intinput("Digite outro valor: ")

    if num1 < num2:
        sys.exit("Número 2 não pode ser maior que 1: num1 < num2")
        
    verificar = identy_par_impar(num1, num2)
                
    print(f"Existem {verificar} números ímpares e pares")
        
def identy_par_impar(n1, n2):
    diferenca = n1 - n2
    ver = diferenca//2
    return ver
    
if __name__ == "__main__":
    main()    

    
    

        
