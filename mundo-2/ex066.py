soma = qntd_numeros = 0
while True:
    numero = int(input('Digite um valor (999 para PARAR): '))

    if numero == 999:
        break
    soma += numero
    qntd_numeros += 1

print(f'A soma dos {qntd_numeros} valores foi {soma}!')
