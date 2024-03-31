print('-' * 40)
print('LOJA SUPER BARATÃO'.center(40))
print('-' * 40)

total_compra = produto_custa_mais_que_1000 = valor_produto_mais_barato = contador_produtos = 0
nome_produto_mais_barato = ''

while True:
    produto = str(input('Nome do produto: ')).strip().title()
    valor = float(input('Preço: R$ '))

    total_compra += valor

    if valor > 1000:
        produto_custa_mais_que_1000 += 1
    
    contador_produtos += 1
    if contador_produtos == 1 or valor < valor_produto_mais_barato:
        nome_produto_mais_barato = produto
        valor_produto_mais_barato = valor

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('FIM DO PROGRAMA'.center(40, '-'))

print(f'''O total da compra foi de R$ {total_compra:.2f}.
Temos {produto_custa_mais_que_1000} produto(s) custando mais de R$ 1000,00.
O produto mais barato foi {nome_produto_mais_barato} que custa R$ {valor_produto_mais_barato:.2f}.''')
