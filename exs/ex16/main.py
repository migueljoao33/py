import random
n2 = str(input("primeiro aluno: "))
n1 = str(input("segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quarto aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("está é a ordem dos alunos: {}" .format(lista))