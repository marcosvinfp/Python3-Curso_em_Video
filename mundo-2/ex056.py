soma_idade = maior_idade_masc = qntd_mulheres_idade_menor_20 = 0
nome_maior_idade_masc = ''

for p in range(0, 4):
    print(f'{"-" * 5} {p + 1}° PESSOA {"-" * 5}')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    soma_idade += idade

    if sexo == 'M' and idade > maior_idade_masc:
        maior_idade_masc = idade
        nome_maior_idade_masc = nome
    
    if sexo == 'F' and idade < 20:
        qntd_mulheres_idade_menor_20 += 1
media_idade = soma_idade / 4

print('-' * 21)

print(f'''A média de idade do grupo é {media_idade}.
O homem mais velho tem {maior_idade_masc} anos e se chama {nome_maior_idade_masc}.
Ao todo são {qntd_mulheres_idade_menor_20} mulheres com menos de 20 anos.''')
