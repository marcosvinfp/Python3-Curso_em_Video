soma_pares = qntd_pares = 0
for n in range(0, 6):
    numero = int(input(f'Digite o {n + 1}° valor: '))
    if numero % 2 == 0:
        soma_pares += numero
        qntd_pares += 1

print(f'Você informou {qntd_pares} números PARES e a soma foi {soma_pares}.')
