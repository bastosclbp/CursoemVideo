from random import shuffle as sff
a1 = str(input('Primeiro(a) aluno(a): '))
a2 = str(input('Segundo(a) aluno(a): '))
a3 = str(input('Terceiro(a) aluno(a): '))
a4 = str(input('Quarto(a) aluno(a): '))
lista = [a1, a2, a3, a4]
sff(lista)
print('A ordem de apresentação será: ')
print(lista)