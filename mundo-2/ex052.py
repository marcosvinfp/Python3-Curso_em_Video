numero = int(input('Digite um número: '))

multiplo = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        multiplo += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(n, '\033[m', end=' ')

print()
print(f'O número {numero} foi divísivel {multiplo} vezes.')

if multiplo == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
