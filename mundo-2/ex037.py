numero = int(input('Digite um número inteiro: '))

opcao = int(input(f'''Escolha uma das bases para conversão:
      [ 1 ] Converter para BINÁRIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL
Sua opção: '''))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a <{bin(numero)}>.')
elif opcao ==2:
    print(f'{numero} convertido para OCTAL é igual a <{oct(numero)}>.')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a <{hex(numero)}>.')
else:
    print(f'Opção inválida, tente novamento!')
