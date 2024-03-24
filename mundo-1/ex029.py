velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print(f'''MULTADO! Você excedeu o limite permitido que é de 80km/h 
Você deve pagar uma multa de R$ {valor_multa:.2f}!''')

print('Tenha um bom dia! Dirija com segurança!')
