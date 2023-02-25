
# MEU
''' n = int(input('Digite um número inteiro: '))
if n / 2 % 1 == 0:
    print('O número informado é PAR.')
else:
    print('O número informado é ÍMPAR.')
'''

# Resolução
número = int(input('Digite um número inteiro: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))
