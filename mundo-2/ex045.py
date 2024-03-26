from random import randint
from time import sleep

'''
Pedra == 0
Papel == 1
Tesoura == 2

            Pedra Papel Tesoura (Computador)
Pedra        0,0   0,1    0,2
Papel        1,0   1,1    1,2
Tesoura      2,0   2,1    2,2
(Jogador)

Resultado == Jogador - Computador

Vitória Jogador -> (1,0); (0,2); (2,1)
      Resultado ->   1  ;   -2 ;  1

Derrota Jogador -> (0,1); (2,0); (1.2)
      Resultado ->  -1  ;   2 ;   -1

  Empate  -> (0,0); (1,1); (2,2)
Resultado ->   0  ;   0 ;    0
'''

print(f'{"-" * 10} JO-KEN-PÔ {"-" * 10}')

itens = ('PEDRA', 'PAPEL', 'TESOURA')

bot = randint(0, 2)
player = int(input('''Suas opções 
        [ 0 ] Pedra
        [ 1 ] Papel
        [ 2 ] Tesoura
        Qual é a sua jogada? '''))

sleep(0.8)
print('JO')

sleep(0.8)
print('KEN')

sleep(0.8)
print('PÔ!!!')

print('-=' * 10)
print(f'''Computador jogou {itens[bot]}
Jogador jogou {itens[player]}''')
print('-=' * 10)

resultado_partida = player - bot

if resultado_partida == 0:
    print('Empate!')
elif resultado_partida in (-2, 1):
    print('Jogador venceu!')
elif resultado_partida in (-1, 2):
    print('Computador perdeu!')
