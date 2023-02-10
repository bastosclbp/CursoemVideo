n = float(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do número {} é {}. \nO triplo do número {} é {}. \nA raiz quadrada do número {} é {:.2f}.'.format(n, d, n, t, n, r))
#DICA
#print('O dobro do número {} é {}. \nO triplo do número {} é {}. \nA raiz quadrada do número {} é {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
#print('O dobro do número {} é {}. \nO triplo do número {} é {}. \nA raiz quadrada do número {} é {:.2f}.'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))