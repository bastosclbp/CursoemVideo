from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))

'''hipo = (co ** 2 + ca ** 2) ** (1/2)
print('Para os valores dos catetos {} e {} a hipotenusa é: {:.2f}'.format(co, ca, hipo))'''