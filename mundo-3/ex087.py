matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

print('-=' * 15)

soma_pares = soma_3_coluna = maior_2_linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        
        if coluna == 2:
            soma_3_coluna += matriz[linha][coluna]
        
        if linha == 1:

            if coluna == 0:
                maior_2_linha = matriz[linha][coluna]

            elif matriz[linha][coluna] > maior_2_linha:
                maior_2_linha = matriz[linha][coluna]

        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()

print('-=' * 15)

print(f'''A soma dos valores pares é {soma_pares}.
A soma dos valores da terceira coluna é {soma_3_coluna}.
O maior valor da segunda linha é {maior_2_linha}.''')
