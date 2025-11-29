distancia = float(input("Distancia em KM: "))
litros = float(input("Quantidade em Litros: "))


km_l = distancia/litros

if km_l < 8:
    print("Venda o carro")
elif km_l < 14:
    print("Economico")
else:
    print("Super economico")