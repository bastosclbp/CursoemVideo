from random import choice
a1 = str(input('Escreva o nome do(a) primeiro(a) aluno(a): '))
a2 = str(input('Escreva o nome do(a) segundo(a) aluno(a): '))
a3 = str(input('Escreva o nome do(a) terceiro(a) aluno(a): '))
a4 = str(input('Escreva o nome do(a) quarto(a) aluno(a): '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno(a) escolhido(a) foi o(a): {}'.format(escolhido))