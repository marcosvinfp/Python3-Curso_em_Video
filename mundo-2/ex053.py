frase = str(input('Digite uma frase: ')).strip().lower()

frase_tratada = ('').join(frase.split())
frase_inversa = frase_tratada[-1::-1]

print(f'O inverso de {frase_tratada} é {frase_inversa}.')

palindromo = frase_tratada == frase_inversa
if palindromo:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
