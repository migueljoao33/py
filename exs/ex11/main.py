largura = float(input("largura da parede: "))
altura = float(input("altura da parede: "))
m2 = largura * altura
tinta = m2 / 2
print("sua parede tem a dimensão de {} x {}, com isso calculamos que sua área é de {}m² e você vai precisar de {}l de tinta" .format(largura, altura, m2, tinta))