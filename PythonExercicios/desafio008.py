medida = float(input('Digite quantos metros são: '))
cm = medida * 100
mm = medida * 1000
#print('O valor de {} metros em centímetros é {:.0f}cm \nO valor de {} metros em milímetros é {:.0f}mm'.format(medida, cm, medida, mm))
#Desafio ++
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
print('O valor de {} metros em Quilômetros é {}km.'.format(medida, km))
print('O valor de {} metros em Hectômetros é {}hm.'.format(medida, hm))
print('O valor de {} metros em Decâmetros é {}dam.'.format(medida, dam))
print('O valor de {} metros em Decímetros é {:.0f}dm.'.format(medida, dm))
print('O valor de {} metros em Centímetros é {:.0f}cm.'.format(medida, cm))
print('O valor de {} metros em Milímetros é {:.0f}mm.'.format(medida, mm))

