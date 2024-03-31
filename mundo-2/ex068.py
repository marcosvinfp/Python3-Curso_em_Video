from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))

qntd_vitorias = 0
while True:
    print('-=' * 15)
    player_numero = int(input('Diga um valor: '))
    player_escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    bot_numero = randint(0, 9)
    soma_numero_player_bot = player_numero + bot_numero

    par = soma_numero_player_bot % 2 == 0
    if par:
        par_impar = 'PAR'
    else:
        par_impar = 'ÍMPAR'

    print('-' * 30)
    print(f'Você jogou {player_numero} e o computador {bot_numero}. Total {soma_numero_player_bot} DEU {par_impar}.')
    print('-' * 30)

    vitoria = (par == True and player_escolha == 'P') or (par == False and player_escolha == 'I')
    if vitoria:
        print('Você VENCEU!')
        qntd_vitorias += 1
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {qntd_vitorias} vez(es).')
