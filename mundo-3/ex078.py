numeros = list()
for posicao in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {posicao}: ')))

print('-=' * 15)

print(f'Você digitou os valores {numeros}.')

menor = min(numeros)
print(f'O menor valor digitado foi {menor} nas posições', end=' ')

for pos in range(0, len(numeros)):
    if numeros[pos] == menor:
        print(pos, end='... ')
print()

maior = max(numeros)
print(f'O maior valor digitado foi {maior} nas posições', end=' ')

for pos in range(0, len(numeros)):
    if numeros[pos] == maior:
        print(pos, end='... ')
print()
