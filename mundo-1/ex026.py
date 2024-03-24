frase = str(input('Digite uma frase: ')).strip().upper()

qntd_letra_A = frase.count('A')
primeira_letra_A = frase.find('A') + 1
ultima_letra_A = frase.rfind('A') + 1

print(f'''A letra "A" aparece {qntd_letra_A} vezes na frase.
A primeira letra "A" apareceu na posição {primeira_letra_A}.
A última letra "A" apareceu na posição {ultima_letra_A}.''')
