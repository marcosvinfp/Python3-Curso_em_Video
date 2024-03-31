from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

tentativas = 0
bot = randint(0, 10)

while True:
    player = int(input('Qual é seu palpite? '))
    tentativas += 1

    palpite_maior = player > bot
    palpite_menor = player < bot
    acertou_palpite = player == bot

    if acertou_palpite:
        print(f'Você acertou com {tentativas} tentativa(s). Parabéns!')
        break
    elif palpite_menor:
        print('Mais...', end=' ')
    elif palpite_maior:
        print('Menos...', end=' ')
    print('Tente mais uma vez.')
