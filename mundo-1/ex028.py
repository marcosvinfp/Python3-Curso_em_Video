from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

bot = randint(0, 5)
player = int(input('Em que número eu pensei? '))

sleep(0.8)
print('PROCESSANDO...')
sleep(1.2)

if bot == player:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Pensei no número {bot} não no {player}!')
