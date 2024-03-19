algo = str(input('Digite algo: '))
print(f'''O tipo primitivo desse valor é {type(algo)}.
Só tem espaços? {algo.isspace()}
É um número? {algo.isnumeric()}
É alfabético? {algo.isalpha()}
É alfanumérico? {algo.isalnum()}
Está em maiúsculas? {algo.isupper()}
Está em minúsculas? {algo.islower()}
Está capitalizada? {algo.istitle()}''')
