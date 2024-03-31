qntd_numeros = soma = 0

continuar = 'S'
while continuar != 'N':
    numero = int(input('Digite um número: '))
    qntd_numeros += 1
    soma += numero

    if qntd_numeros == 1:
        menor = maior = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    continuar = str(input('Quer continuar? ')).strip().upper()[0]

media = soma / qntd_numeros

print(f'''Você digitou {qntd_numeros} números e a média foi {media}.
O menor valor foi {menor} e o maior foi {maior}.''')
