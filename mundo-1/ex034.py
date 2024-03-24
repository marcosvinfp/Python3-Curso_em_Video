salario = float(input('Qual é o salário do funcionário? R$ '))

salario_com_aumento = salario * (1.15 if salario <= 1250 else 1.10)

print(f'Quem ganhava R$ {salario:.2f} passa a ganhar agora R$ {salario_com_aumento:.2f}.')
