primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
terceiro_valor = int(input('Terceiro valor: '))

menor = maior = primeiro_valor

# Testes p/ menor valor
if segundo_valor < menor:
    menor = segundo_valor
if terceiro_valor < menor:
    menor = terceiro_valor

# Testes p/ maior valor
if segundo_valor > maior:
    maior = segundo_valor
if terceiro_valor > maior:
    maior = terceiro_valor

print(f'''O menor valor digitado foi {menor}.
O maior valor digitado foi {maior}.''')
