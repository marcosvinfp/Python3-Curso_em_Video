pilha_parenteses = list()

expressao = str(input('Digite uma expressão: ')).strip()

for caractere in expressao:
    if caractere == '(':
        pilha_parenteses.append('(')
    elif caractere == ')':
        if len(pilha_parenteses) > 0:
            pilha_parenteses.pop()
        elif len(pilha_parenteses) == 0:
            pilha_parenteses.append(')')
            break

if len(pilha_parenteses) == 0:
    print('Sua expressão é válida!')
elif len(pilha_parenteses) != 0:
    print('Sua expressão é inválida!')
