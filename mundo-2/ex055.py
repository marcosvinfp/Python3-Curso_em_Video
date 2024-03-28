for p in range(0, 5):
    massa = float(input(f'Peso da {p + 1}° pessoa: '))

    if p == 0:
        menor_massa = maior_massa = massa
    else:
        if massa < menor_massa:
            menor_massa = massa
        if massa > maior_massa:
            maior_massa = massa

print(f'''O menor peso lido foi de {menor_massa}kg.
O maior peso lido foi de {maior_massa}kg.''')
