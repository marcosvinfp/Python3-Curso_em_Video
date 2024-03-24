distancia_viagem = float(input('Qual é a distância da sua viagem? '))

custo_viagem = distancia_viagem * (0.5 if distancia_viagem <= 200 else 0.45)

print(f'''Você está prestes a começar uma viagem de {distancia_viagem:.1f}km.
E o preço da sua viagem será de R$ {custo_viagem:.2f}.''')
