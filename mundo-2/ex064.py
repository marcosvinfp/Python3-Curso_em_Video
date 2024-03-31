soma = qntd_numeros = numero = 0
while numero != 999:
    numero = int(input('Digite um número [999 para PARAR]: '))

    if numero != 999:
        soma += numero
        qntd_numeros += 1

print(f'Você digitou {qntd_numeros} números e a soma entre eles foi {soma}.')
