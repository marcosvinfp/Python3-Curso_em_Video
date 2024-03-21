from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'''O ângulo de {angulo:.1f} tem o SENO de {seno:.2f}
O ângulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}
O ângulo de {angulo:.1f} tem o TANGENTE de {tangente:.2f}''')
