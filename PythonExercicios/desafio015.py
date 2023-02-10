km = float(input('Qual o KM percorrido com o carro? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
diaria = dias * 60
rodado = km * 0.15
print('Por diaria foi gasto R${:.2f} e por KM foi gasto R${:.2f} dando um total de: R${:.2f}'.format(diaria, rodado, diaria + rodado))