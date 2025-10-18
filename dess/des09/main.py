frase = str(input("digite uma frase: ")).upper()
print("a letra a apareceu {}" .format(frase.count('A')))
print("a primeira letra a aparaceu em {}" .format(frase.find('A')+1))
print("a ultima letra a aparaceu em {}" .format(frase.rfind('A')+1))