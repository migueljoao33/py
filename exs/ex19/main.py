# idade = int(input("quantos anos tem o seu carro? "))
# if idade <= 3:
#     print("novo")
# else:
#     print("velho")
# print("novo" if idade<= 3 else "velho")

# nome = str(input("qual o seu nome? "))
# if nome == "joao miguel":
#     print("você tem um nome lindo!")
# else:
#     print("que nome sem graça")
# print("olá {}" .format(nome))

escola = str(input("qual o nome da sua escola? "))
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print("você passou de ano com a nota {}, parabéns!" .format(media))
else:
    print("sinto muito mas você está de recuperação, com a nota {}" .format(media))
print("{}" .format(escola))