largura = float(input('Informe a Largura da parede em metros: '))
altura = float(input('Informe a Altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Para pintar a sua parede de {}m² será necessário {}l de tinta.'.format(area, tinta))