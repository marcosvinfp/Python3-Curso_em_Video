numeros = list()

for i in range(0, 5):
    num = int(input('Digite um valor: '))

    if i == 0 or num >= numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        for pos, numero in enumerate(numeros):
            if num <= numero:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break

print('-=' * 15)
print(f'Os valores digitados em ordem foram {numeros}.')
