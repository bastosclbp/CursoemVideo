velocidade = float(input('Qual a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Você foi multado! E vai lhe custar R${:.2f}'.format(multa))
else:
    print('Você não foi multado.')
