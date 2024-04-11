cadastro = list()
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')).strip().title())
    pessoa.append(float(input('Peso (Kg): ')))

    if len(cadastro) == 0:
        menor_peso = maior_peso = pessoa[1]
    elif menor_peso > pessoa[1]:
        menor_peso = pessoa[1]
    elif maior_peso < pessoa[1]:
        maior_peso = pessoa[1]
    
    cadastro.append(pessoa[:])
    pessoa.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break

    if continuar == 'N':
        break

print('-=' * 15)
print(f'Ao todo você cadastrou {len(cadastro)} pessoas.')

print(f'O menor peso foi de {menor_peso} kg. Peso de ', end='')
for pess in cadastro:
    if pess[1] == menor_peso:
        print(f'[{pess[0]}]', end=' ')
print()

print(f'O maior peso foi de {maior_peso} kg. Peso de ', end='')
for pess in cadastro:
    if pess[1] == maior_peso:
        print(f'[{pess[0]}]', end=' ')
print()
