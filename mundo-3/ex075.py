numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o último número: ')))

print(f'''Você digitou os valores: {numeros}.
O valor 9 apareceu {numeros.count(9)} veze(s).''')

if 3 in numeros:
    print('O valor 3 apareceu na', end=' ')
    for p, n in enumerate(numeros):
        if n == 3:
            print(f'{p + 1}°', end=' ')
    print('posição.')
else:
    print('O valor 3 não foi digitado.')

print('Os valores pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('.')
