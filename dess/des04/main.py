import math
co = float(input("cateto oposto: "))
ca = float(input("cateto adjacente: "))
# isso tmb pode ser isso (linha 7)
# hi = (co ** 2 + ca **2) ** (1/2)
# print("hipotenusa = {}" .format(hi))
print(math.hypot(co, ca))