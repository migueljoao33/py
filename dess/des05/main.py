# tmb pode ser assim
# from math import radians, sin, cos, tan
import math
ang = float(input("digite um número: "))
seno = math.sin(math.radians(ang))
print("o angulo de {} tem o seno de {:.2f}" .format(ang, seno))
cosseno = math.cos(math.radians(ang))
print("o angulo de {} tem o cosseno de {:.2f}" .format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print("o angulo de {} tem o tangente de {:.2f}" .format(ang, tangente))