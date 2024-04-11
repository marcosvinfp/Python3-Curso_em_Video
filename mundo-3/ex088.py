from random import randint
from time import sleep

print('-' * 32)
print('JOGA NA MEGA-SENA'.center(30))
print('-' * 32)

qntd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'{"-=" * 3} SORTEANDO {qntd_jogos} JOGOS {"-=" * 3}')

jogo = list()
cartela_jogos = list()

for j in range(0, qntd_jogos):
    while len(jogo) < 6:
        sorteio = (randint(1, 61))
        if sorteio not in jogo:
            jogo.append(sorteio)

    jogo.sort()
    cartela_jogos.append(jogo[:])
    jogo.clear()

for indice, j in enumerate(cartela_jogos):
    sleep(0.8)
    print(f'Jogo {indice + 1:2}: {j}')
print(f'{"=-" * 5}< BOA SORTE! >{"=-" * 5}')
