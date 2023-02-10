preco = float(input('Infome o preço do produto: '))
desconto = preco - (preco * 5 / 100)
print("O seu produto com 5% de desconto custará: R${:.2f}".format(desconto))
