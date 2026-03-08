import time
import os

frames = ["Eu",
"te",
"amo",
"minha",
"querida",
"mãe",
":)",
]

for frame in frames:
    time.sleep(0.65)
    
    print(frame)
    
def main():    
    while True:
        time.sleep(1)
        tenta = str(input("Quer ver de novo?S/N\n")).lower()
        if tenta == "s":
            os.system("clear")
            code()
            continue
       
    
        elif tenta == "n":
            break
        
def code():
    for frame in frames:
     time.sleep(0.65)
     print(frame)        
main()
    

    
