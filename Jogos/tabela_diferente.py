guardar = []

with open('info.csv') as file:
    for linha in file:
        estado, quantidade = linha.rstrip().split(',')
        
        infos = {'estados' : estado,
       
'aura' : quantidade,
}

        guardar.append(infos)
        
   
   
for coisas in guardar:
    nomes_st = coisas['estados']
    numeros_st = int(coisas['aura'])
    print(f'Os estados de {nomes_st} tem {numeros_st} de aura')
    
    
    

