while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)

    if numero < 0:
        break

    for n in range(1, 11):
        print(f'{numero:3} X {n:3} == {numero * n:3}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
