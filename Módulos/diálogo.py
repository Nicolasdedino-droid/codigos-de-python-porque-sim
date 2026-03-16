import sys
import time

def main():
    
   dialogo(0.1, "Hello everynyan! how are u? fine! Xanqui u.") 
    
    
def dialogo(tempo, texto):
    for letras in texto:
        sys.stdout.write(letras)
        sys.stdout.flush()
        time.sleep(tempo)
    print()
        
        
if __name__ == "__main__":
    main()