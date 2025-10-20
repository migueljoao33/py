ano = int(input("qual ano quer analisar? "))
if ano % 4 == 0:
    print("a ano {} é um ano bissexto" .format(ano))
else:
    print("a ano {} não é um ano bissexto" .format(ano))