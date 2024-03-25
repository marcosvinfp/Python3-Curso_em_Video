primeira_nota = float(input('Priemria nota: '))
segunda_nota = float(input('Segunda nota: '))
media_notas = (primeira_nota + segunda_nota) / 2

print(f'Como resultado das notas {primeira_nota:.1f} e {segunda_nota:.1f}, a média do aluno é {media_notas:.1f}.')

if media_notas < 5:
    print('O aluno está REPROVADO.')
elif media_notas <= 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
