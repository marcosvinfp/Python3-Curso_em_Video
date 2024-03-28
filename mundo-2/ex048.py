soma_numeros = qntd_numeros = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma_numeros += numero
        qntd_numeros += 1

print(f'A soma de todos os {qntd_numeros} valores solicitados é {soma_numeros}.')
