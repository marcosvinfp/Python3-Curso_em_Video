nome_completo = str(input('Digite seu nome completo: ')).strip().title()

print('Analisando seu nome...')

qntd_letras_nome_completo = len(nome_completo) - nome_completo.count(' ')
primeiro_nome = nome_completo[0:nome_completo.find(' ')]

print(f'''Seu nome em maiúsculas é {nome_completo.upper()}.
Seu nome em minúsculas é {nome_completo.lower()}.
Seu nome tem ao todo {qntd_letras_nome_completo} letras.
Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.''')
