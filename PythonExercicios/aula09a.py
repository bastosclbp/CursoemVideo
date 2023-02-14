frase = 'Curso em Vídeo Python'
'''Fatiamento'''
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])  # pula de 2 em 2.
print(frase[:5])  # do início.
print(frase[15:])  # até o final.
print(frase[9::3])  # vai até o final e pula de 3 em 3.
'''Análise'''
print(len(frase))  # lê o comprimento.
print(frase.count('o'))  # conta quantas vezes aparece.
# conta quantas vezes aparece em uma parte específica.
print(frase.count('o', 0, 13))
print(frase.find('deo'))  # indica / procura onde começa.
print(frase.find('Android'))  # Resultado: -1 indica que não foi encontrado
print('Curso' in frase)  # True ou False
print(frase.replace('Python', 'Android'))  # substitui Python por Android
'''Transformação'''
print(frase.upper())  # Tudo em maiúsculo
print(frase.lower())  # Tudo em minúsculo
print(frase.capitalize())  # Só a primeira caracter em maiúsculo
print(frase.title())  # Caracter de cada palavra em maiúsculo
frase = '   Aprenda Python  '
print(frase.strip())  # Elimina espaços desnecessários
print(frase.rstrip())  # Remove os espaços da direita (final)
print(frase.lstrip())  # Remove os espaços da esquerda (início)
'''Divisão'''
frase = 'Curso em Vídeo Python'
print(frase.split())  # Divide os espaços gerando uma lista.
'''Junção'''
n = frase.split()
print('-'.join(n))  # Junta a string dividida separando com traço
