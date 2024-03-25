valor_imovel = float(input('Valor do imóvel: R$ '))
tempo_financiamento_anos = int(input('Quantos anos de financiamento? '))
salário_comprador = float(input('Salário do comprador: R$ '))

parcela_imovel = valor_imovel / (tempo_financiamento_anos * 12)
condicao = 'APROVADO' if parcela_imovel <= (salário_comprador * 0.3) else 'REPROVADO'

print(f'''Para pagar uma casa de R$ {valor_imovel:.2f} em {tempo_financiamento_anos} anos a parcela será de R$ {parcela_imovel:.2f}.
EMPRÉSTIMO {condicao}!''')
