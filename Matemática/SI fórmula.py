while True:
    try:
        n = int(input('Digite o valor de N: '))
    except ValueError:
        continue
    if n < 3:
         print('Não é polígono!')
         continue
    else:
         print(f'A soma dos ângulos internos da forma é {(n - 2) * 180}')