campeonato = ('Palmeiras', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Botafogo',
              'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
              'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Santos',
              'Vasco', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {campeonato}')

print('-=' * 15)
print(f'Os 5 primeiros são: {campeonato[:5]}')

print('-=' * 15)
print(f'Os 4 últimos são: {campeonato[-4:]}')

print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(campeonato)}')

print('-=' * 15)
if 'Chapecoense' in campeonato:
    print(f'O Chapecoense está na {campeonato.index("Chapecoense") + 1}° posição.')
else:
    print(f'O Chapecoense não se classificou.')
