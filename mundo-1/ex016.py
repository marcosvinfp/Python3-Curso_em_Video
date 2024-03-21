from math import trunc
# Alternativamente poderia-se usar o método int()

numero = float(input('Digite um valor: '))

print(f'O valor digitado foi {numero} e a sua porção inteira é {trunc(numero)}.')
