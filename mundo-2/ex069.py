total_pessoas_mais_18 = total_homem = mulher_menos_20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-' * 30)

    idade = int(input('Idade: '))

    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
    
    if idade > 18:
        total_pessoas_mais_18 += 1
    if sexo == 'M':
        total_homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1

    print('-' * 30)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print(f'''Total de pessoas com mais de 18 anos: {total_pessoas_mais_18}.
Ao todo temos {total_homem} homem(ens) cadastrado(s).
E temos {mulher_menos_20} mulher com menos de 20 anos.''')
