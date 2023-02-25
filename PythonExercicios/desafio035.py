seg1 = float(input('Informe o tamanho do primeiro segmento: '))
seg2 = float(input('Informe o tamanho do segundo segmento: '))
seg3 = float(input('Informe o tamanho do terceiro segmento: '))
if seg2 + seg3 > seg1 and seg1 + seg3 > seg2 and seg1 + seg2 > seg3:
    print('O triângulo pode ser gerado!')
else:
    print('O triânglo NÃO pode ser gerado!')
