algo = str(input('\033[1;31mDigite algo: '))
print(f'''\033[mO tipo primitivo desse valor é \033[7;32m{type(algo)}\033[m.
\033[4;33mSó tem espaços? {algo.isspace()}\033[m
\033[34mÉ um número? {algo.isnumeric()}
\033[35mÉ alfabético? {algo.isalpha()}
\033[36mÉ alfanumérico? {algo.isalnum()}
\033[37mEstá em maiúsculas? {algo.isupper()}
\033[31mEstá em minúsculas? {algo.islower()}
\033[32mEstá capitalizada? {algo.istitle()}\033[m''')
