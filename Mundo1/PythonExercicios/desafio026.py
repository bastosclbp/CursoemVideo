texto = str(input('Digite uma frase: ')).upper().strip()
print(texto.count('A'))
print(texto.find('A')+1)  # +1 para ficar com númeração a partir do 1
print(texto.rfind('A')+1)  # +1 para ficar com a númeração a partir do 1
