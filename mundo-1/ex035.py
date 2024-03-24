print('-=-' * 20)
print('Analisador de Triângulos'.center(60))
print('-=-' * 20)

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

# Atribuição da variável pode_nao_pode FORMAR triângulo
if (segmento1 < segmento2 + segmento3) and (segmento2 < segmento1 + segmento3) and (segmento3 < segmento1 + segmento2):
    pode_nao_pode = 'PODEM FORMAR'
else:
    pode_nao_pode = 'NÃO PODEM FORMAR'

print(f'Os segmentos acima {pode_nao_pode} um triângulo!')
