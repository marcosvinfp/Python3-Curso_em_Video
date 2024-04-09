numeros = list()
while True:
    numero = int(input(f'Digite um valor: '))

    if numero in numeros:
        print('Valor duplicado! Não adicionado...')
    else:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-=' * 15)
numeros.sort()
print(f'Você digitou os valores {numeros}.')
