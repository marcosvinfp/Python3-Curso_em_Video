print('=' * 40)
print('BANCO CEV'.center(40))
print('=' * 40)

saque = int(input('Qual valor você quer sacar? R$ '))

cedulas_disponiveis = (50, 20, 10, 1)

valor_processado = saque
total_cedulas = varredor = 0

while valor_processado > 0:
    cedula = cedulas_disponiveis[varredor]
    varredor += 1

    if cedula <= valor_processado:
        total_cedulas = valor_processado // cedula
        valor_processado -= total_cedulas * cedula
        
        print(f'Total de {total_cedulas:2} cédulas de R$ {cedula:5.2f}')

print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
