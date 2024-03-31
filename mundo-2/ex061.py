print('=' * 30)
print('10 TERMOS DE UMA PA'.center(30))
print('=' * 30)

primeiro_termo_pa = int(input('Primeiro termo: '))
razao_pa = int(input('Razão: '))
decimo_primeiro_termo_pa = primeiro_termo_pa + (razao_pa * 10)

termo = primeiro_termo_pa
while termo < decimo_primeiro_termo_pa:
    print(termo, end=' -> ')
    termo += razao_pa
print('FIM')
