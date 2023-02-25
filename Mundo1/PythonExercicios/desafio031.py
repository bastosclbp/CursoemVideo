# Meu
'''viagem = float(input('Qual a distância da viagem em Km? '))
if viagem <= 200:
    print('Sua viagem vai custar: R${:.2f}'.format(viagem * 0.50))
else:
    print('Sua viagem vai custar: R${:.2f}'.format(viagem * 0.45))
'''
# Resolução
'''distância = float(input('Qual é a distância da sua viagem em Km? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))
'''
# Simplificação
distância = float(input('Qual é a distância da sua viagem em Km? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))
