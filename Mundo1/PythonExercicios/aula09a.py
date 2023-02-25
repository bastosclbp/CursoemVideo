frase = 'Curso em Vídeo Python'
'''Fatiamento'''
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])  # 9 até 21, pulando de 2 em 2.
print(frase[:5])  # Do início até 5.
print(frase[15:])  # Do 15 até o final.
print(frase[9::3])  # Do 9 até o final e pula de 3 em 3.
print(frase[::2])  # Não sei o inicio nem o final, mas pula de 2 em 2.
'''Análise'''
print(len(frase))  # lê o comprimento.
print(frase.count('o'))  # conta quantas vezes aparece.
# conta quantas vezes aparece em uma parte específica.
print(frase.count('o', 0, 13))
print(frase.find('deo'))  # indica / procura onde começa.
print(frase.find('Android'))  # Resultado: -1 indica que não foi encontrado.
print('Curso' in frase)  # True ou False.
print(frase.replace('Python', 'Android'))  # substitui Python por Android.
'''Transformação'''
print(frase.upper())  # Tudo em maiúsculo.
print(frase.lower())  # Tudo em minúsculo.
print(frase.capitalize())  # Só a primeira caracter em maiúsculo.
print(frase.title())  # Caracter de cada palavra em maiúsculo.
frase = '   Aprenda Python  '
print(frase.strip())  # Elimina espaços desnecessários.
print(frase.rstrip())  # Remove os espaços da direita (final).
print(frase.lstrip())  # Remove os espaços da esquerda (início).
'''Divisão'''
frase = 'Curso em Vídeo Python'
print(frase.split())  # Divide os espaços gerando uma lista.
'''Junção'''
n = frase.split()
print('-'.join(n))  # Junta a string dividida separando com traço.
'''DICAS'''
print('''xxxxxxxxxxxx
xxxxxxxxxxx
xxxxxxxx
xxxxxxx''')  # ''' ''' Printa uma frase muito grande.
print(frase.upper().count('O'))  # Primeiro poem em maiúsculo para contar.
# Coloca a frase em minúsculo e depois procura.
print(frase.lower().find('vídeo'))
# Divide a frase e mostra só a primeira palavra.
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])  # Pega a segunda palavra e mostra a sua terceira letra.
