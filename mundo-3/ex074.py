from random import randint

numeros_sorteados = (randint(0, 9),
                     randint(0, 9),
                     randint(0, 9),
                     randint(0, 9),
                     randint(0, 9))

print('Os números sorteados foram:', end=' ')

for n in numeros_sorteados:
    print(n, end=' ')
print()

print(f'''O menor valor sorteado foi {min(numeros_sorteados)}.
O maior valor sorteado foi {max(numeros_sorteados)}.''')
