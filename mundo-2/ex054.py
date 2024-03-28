from datetime import date

ano_atual = date.today().year
qntd_menor_idade = qntd_maior_idade = 0

for p in range(0, 7):
    ano_nasc = int(input(f'Em que ano a {p + 1}° pessoa nasceu? '))

    idade = ano_atual - ano_nasc
    if idade >= 21:
        qntd_maior_idade += 1
    else:
        qntd_menor_idade += 1

print(f'''Ao todo tivemos {qntd_maior_idade} pessoas maiores de idade.
E também tivemos {qntd_menor_idade} pessoas menores de idade.''')
