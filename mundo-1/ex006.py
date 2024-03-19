numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = pow(numero, 1/2)

print(f'''O dobro de {numero} vale {dobro}.
O triplo de {numero} vale {triplo}.
A raíz quadrada de {numero} vale {raiz:.2f}''')
