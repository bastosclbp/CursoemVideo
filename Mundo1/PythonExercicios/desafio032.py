from datetime import date
# Meu
'''ano = int(input('Informe o ano: '))
resultado = ano % 4
if resultado == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
'''

# Resolução
ano = int(input('Que ano quer analisar? Coloque 0 par analuisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
