salário = float(input('Informe o valor do seu salário: '))
if salário > 1250:
    aumento = (salário * 10) / 100
else:
    aumento = (salário * 15) / 100
print('Seu aumento será de: R${:.2f}'.format(aumento))
