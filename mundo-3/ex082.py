numeros_conjunto = list()
numeros_pares = list()
numeros_impares = list()

while True:
    numero = int(input('Digite um número: '))

    numeros_conjunto.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-=' * 15)

numeros_conjunto.sort()
numeros_pares.sort()
numeros_impares.sort()

print(f'''A lista completa é {numeros_conjunto}.
A lista de pares é {numeros_pares}.
A lista de ímpares é {numeros_impares}.''')
