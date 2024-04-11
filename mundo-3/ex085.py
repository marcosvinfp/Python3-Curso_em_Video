numeros = [[], []]

for i in range(0, 7):
    numero = int(input(f'Digite o {i + 1}° valor: '))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print('-=' * 15)
numeros[0].sort()
numeros[1].sort()

print(f'''Os valores pares digitados foram: {numeros[0]}.
Os valores ímpares digitados foram: {numeros[1]}.''')
