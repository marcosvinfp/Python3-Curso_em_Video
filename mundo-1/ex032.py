from datetime import date

ano_analisado = int(input('Qual ano deseja analisar? Coloque 0 para analisar o ano atual: '))
ano_analisado = date.today().year if ano_analisado == 0 else ano_analisado

# Variável -> É ou NÃO É Bissexto
e_não_e = 'É' if (ano_analisado % 4 == 0 and ano_analisado % 100 != 0) or (ano_analisado % 400 == 0) else 'NÃO É'

print(f'O ano {ano_analisado} {e_não_e} BISSEXTO.')
