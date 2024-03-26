print('-=-' * 20)
print('Analisador de Triângulos v2.0'.center(60))
print('-=-' * 20)

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

condicao_existencia_triangulo = (segmento1 < segmento2 + segmento3) and (segmento2 < segmento1 + segmento3) and (segmento3 < segmento1 + segmento2)

equilatero = segmento1 == segmento2 == segmento3
isosceles = segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3
escaleno = segmento1 != segmento2 and segmento1 != segmento3 and segmento2 != segmento3

if condicao_existencia_triangulo:
    if equilatero:
        tipo_triangulo = 'EQUILÁTERO'
    elif isosceles:
        tipo_triangulo = 'ISÓSCELES'
    elif escaleno:
        tipo_triangulo = 'ESCALENO'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo_triangulo}!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
