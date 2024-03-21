largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
volume_tinta= area / 2

print(f'''Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e sua área é {area:.3f}m².
Para pintar essa parede, você precisará de {volume_tinta:.4f}L de tinta.''')
