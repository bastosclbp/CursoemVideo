
# MEU
'''from random import randrange
n = int(input('Tente advinhar o número escolhido entre 0 e 5: '))
i = randrange(6)
if n == i:
    print('Você venceu!')
else:
    print('Você perdeu! O número sorteado foi: {}'.format(i))'''


# Resolução
from random import randint
from time import sleep
computador = randint(0, 5)  # sorteia o número
print('-=-' * 20)
print('Tente advinha o número escolhido entre 0 e 5... ')
print('-=-' * 20)
escolhido = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if escolhido == computador:
    print('Parabéns! Você acertou!!!')
else:
    print('Você errou! O número escolhido foi: {}'.format(computador))
