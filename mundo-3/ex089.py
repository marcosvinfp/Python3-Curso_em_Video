turma = list()

while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    turma.append([nome, media, [nota1, nota2]])

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":15}{"MÉDIA"}')
print('-' * 30)

for indice, aluno in enumerate(turma):
    print(f'{indice:<4}{aluno[0]:15}{aluno[1]:5.1f}')

while True:
    print('-' * 30)
    while True:
        mostrar_notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if mostrar_notas in range(0, len(turma)) or mostrar_notas == 999:
            break
    if mostrar_notas == 999:
        break

    print(f'Notas de {turma[mostrar_notas][0]} são {turma[mostrar_notas][2]}.')

print(f'''FINALIZANDO ...
<<< Volte sempre! >>>''')
