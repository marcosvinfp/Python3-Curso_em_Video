lista_produtos = ('lápis', 1.75,
                  'borracha', 2.00,
                  'caderno', 15.90,
                  'estojo', 25.00,
                  'transferidor', 4.20,
                  'compasso', 9.99,
                  'mochila', 120.32,
                  'canetas', 22.30,
                  'livro', 34.90)

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)

for posicao in range(0, len(lista_produtos)):
    if posicao % 2 == 0:
        print(f'{lista_produtos[posicao].title():.<30}', end='')
    else:
        print(f'R$ {lista_produtos[posicao]:>7.2f}')
print('-' * 40)
