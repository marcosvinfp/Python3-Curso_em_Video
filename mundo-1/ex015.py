dias_alugados = int(input('Quantos dias alugados? '))
km_rodado = float(input('Quantos quilômetros rodados? '))
custo_total = (dias_alugados * 60) + (km_rodado * 0.15)

print(f'O total a pagar é de R$ {custo_total:.2f}.')
