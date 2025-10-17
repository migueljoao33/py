import random
n1 = str(input("digite um nome: "))
n2 = str(input("digite outro nome: "))
n3 = str(input("digite outro nome: "))
n4 = str(input("digite outro nome: "))
lista = [n1, n2, n3, n4]
el = random.choice(lista)
print("o aluno escolhido foi {}" .format(el))