print(f'{"=" * 11} LOJAS GUANABARA {"=" * 11}')

valor_compra = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO:
      [ 1 ] À vista dinheiro/cheque
      [ 2 ] À vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão
''')
forma_pagamento = int(input('Qual opção de pagamento? '))

if forma_pagamento == 1:
    valor_final = valor_compra * 0.9
elif forma_pagamento == 2:
    valor_final = valor_compra * 0.95
elif forma_pagamento == 3:
    num_parcelas = 2
    valor_final = valor_compra
elif forma_pagamento == 4:
    num_parcelas = int(input('Quantas parcelas? '))
    valor_final = valor_compra * 1.2
else:
    valor_final = valor_compra
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

if forma_pagamento == 3 or forma_pagamento == 4:
    valor_parcela = valor_final / num_parcelas
    print(f'Sua compra será parcelada em {num_parcelas}x de R$ {valor_parcela:.2f} COM JUROS.')

print(f'Sua compra de R$ {valor_compra:.2f} vai custar R$ {valor_final:.2f} no total.')
