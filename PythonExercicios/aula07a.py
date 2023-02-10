n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a subtração é {}, o produto é {} e a \n divisão é {:.3f}.'.format(s, su, m, d), end=' ')
print('Divisão inteira {} e potência {}.'.format(di, e))