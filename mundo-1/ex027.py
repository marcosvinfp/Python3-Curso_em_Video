nome_completo = str(input('Digite seu nome completo: ')).strip().title()
nome_split = nome_completo.split()

print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {nome_split[0]}.
Seu último nome é {nome_split[-1]}.''')
