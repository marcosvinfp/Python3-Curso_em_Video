numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez','onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    if numero not in range(0, len(numero_extenso)):
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {numero_extenso[numero]}.')
    
        while True:
            continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if continuar in 'SN':
                break
        if continuar == 'N':
            print('Programa encerrado.')
            break
