from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

tempo_para_alistamento = 18 - idade
ano_alistamento = ano_atual + tempo_para_alistamento

print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')

if tempo_para_alistamento > 0:
    print(f'Ainda faltam {tempo_para_alistamento} anos para o alistamento.\nSeu alistamento será em {ano_alistamento}.')
elif tempo_para_alistamento < 0:
    print(f'Você já deveria ter se alistado há {-tempo_para_alistamento} anos.\nSeu alistamento foi em {ano_alistamento}.')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
