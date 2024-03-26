massa = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = massa / (altura * altura)

print(f'O IMC dessa pessoa é de {imc:.1f}.')

if imc < 18.5:
    print('Você está na faixa ABAIXO DO PESO.')
elif imc < 25:
    print('PARABÉNS! Você está na faixa de PESO IDEAL.')
elif imc < 30:
    print('Você está na faixa de SOBREPESO.')
elif imc < 40:
    print('Você está na faixa de OBESIDADE.')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA, cuidado!')
