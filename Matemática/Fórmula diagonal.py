while True:
    try:
        n = int(input('Valor de N: '))
    except ValueError:
        continue
    if n < 3:
        print('Impossivel.')
        continue
    else:
        print(f'a diagonal da forma de {n} lados vai ser {(n-3)*n/2}')