numeros = list()

while True:
    numeros.append(int(input('Digite um valor: ')))

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-=' * 15)

numeros.sort(reverse=True)

print(f'''Você digitou {len(numeros)} elementos.
Os valores em ordem decrescente são {numeros}.''')

if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
