import time
valor = 0
while True:
    frames = [":)", ":("]
    
    for frame in frames:
        time.sleep(0.3)
        
        print(frame)
        
        valor += 1
        
    
    if valor >= 500:
        print("IDIOT! IDIOT! IDIOT! IDIOT!")
        valor += 10000
    if valor>= 100:
        print("HAHAHAHAHAHA")
        valor += 10
    if valor >= 25:
        print("YOU'RE AN IDIOT!")
    

