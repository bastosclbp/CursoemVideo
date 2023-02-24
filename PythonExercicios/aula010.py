'''nome = str(input('Qual o seu nome? '))
if nome == 'Carlos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''


# Só com if: estrutura simples.
# Com else: estrutura composta.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa. PARABÉNS!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')  # simplificada do if-else
