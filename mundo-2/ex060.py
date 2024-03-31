numero = int(input('Digite um número para calcular seu fatorial: '))

print(f'\nCalculando {numero}! = ', end='')

fatorial = 1
regressiva = numero
while regressiva > 0:
    print(regressiva, end=' x ' if regressiva > 1 else ' = ')
    fatorial *= regressiva
    regressiva -= 1

print(fatorial)
