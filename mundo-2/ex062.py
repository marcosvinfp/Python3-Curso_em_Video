print('=' * 30)
print('10 TERMOS DE UMA PA'.center(30))
print('=' * 30)

primeiro_termo_pa = int(input('Primeiro termo: '))
razao_pa = int(input('Razão: '))

qntd_termos = 0
adicionar_termos = 10
termo = primeiro_termo_pa

while adicionar_termos != 0:
    qntd_termos += adicionar_termos
    ultimo_termo_pa_mais1 = primeiro_termo_pa + (razao_pa * qntd_termos)

    while termo < ultimo_termo_pa_mais1:
        print(termo, end=' -> ')
        termo += razao_pa
    print('PAUSA')

    adicionar_termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'A progressão foi finalizada com {qntd_termos} termos exibidos.')
