d = float(input("digite a kilometragem da sua viagem: "))
if d >= 200:
    preco = d * 0.45
else:
    preco = d * 0.50
print("o valor da viagem é de: R${}" .format(preco))