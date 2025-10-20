import random
n = random.randint(0, 5)
print("pensei em um número de 0 a 5 , tente advinhar!")
j = int(input("em que número eu pensei? "))
if n == j:
    print("parabéns você acertou!")
else:
    print("sinto muito não foi dessa vez, boa sorte na próxima!")