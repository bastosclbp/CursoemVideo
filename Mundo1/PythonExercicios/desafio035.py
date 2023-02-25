import colorama
colorama.init()
seg1 = float(input('\033[1;30;43m Informe o tamanho do primeiro segmento: '))
seg2 = float(input('\033[1;30;43m Informe o tamanho do segundo segmento: '))
seg3 = float(input('\033[1;30;43m Informe o tamanho do terceiro segmento: '))
if seg2 + seg3 > seg1 and seg1 + seg3 > seg2 and seg1 + seg2 > seg3:
    print('\033[1;30;42m O triângulo pode ser gerado!')
else:
    print('\033[1;30;41m O triânglo NÃO pode ser gerado!')
