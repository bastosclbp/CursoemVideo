from math import radians, sin, cos, tan
ang = float(input('Digite o valor do ângulo: '))
sen = sin(radians(ang))
print('O ângulo de {}º tem o SENO de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(ang, tan))