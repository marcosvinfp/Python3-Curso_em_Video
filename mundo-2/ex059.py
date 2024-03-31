from time import sleep

numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    opcao = int(input('''        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa
    >>>>> Qual é a sua opção? '''))

    if opcao == 1:
        soma = numero1 + numero2
        print(f'A soma entre {numero1} + {numero2} é {soma}.')
    elif opcao == 2:
        multiplicacao = numero1 * numero2
        print(f'O resultado de {numero1} X {numero2} é {multiplicacao}.')
    elif opcao == 3:
        if numero1 == numero2:
            print(f'Ambos os valores são iguais!')
        else:
            maior = numero1
            if numero2 > maior:
                maior = numero2
            print(f'Entre {numero1} e {numero2} o maior valor é {maior}.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        numero1 = int(input('Primeiro valor: '))
        numero2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
