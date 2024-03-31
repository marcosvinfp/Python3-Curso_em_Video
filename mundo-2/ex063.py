print('-' * 30)
print('Sequência de Fibonacci'.center(30))
print('-' * 30)

termos = int(input('Quantos termos você quer mostrar? '))

primeiro_termo = 0
segundo_termo = 1

print('~' * 30)

while termos > 0:
    print(primeiro_termo, end=' -> ')

    terceiro_termo = primeiro_termo + segundo_termo

    # Deslocamento da varredura
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    termos -= 1
print('FIM')

print('~' * 30)
