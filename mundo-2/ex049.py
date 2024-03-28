numero = int(input('Digite um número para ver sua tabuada: '))

print('-' * 15)
for i in range(1, 11):
    print(f'{numero:^3} X {i:^3} = {numero * i:^3}')
print('-' * 15)
