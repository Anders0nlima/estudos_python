lista_Ap = ["I", "II", "III", "IV", "V"]
lista_Area = [80, 90, 120, 130, 135]
lista_Preco = [350, 450, 480, 580, 620]

preco_por_area = []

for ap, area, preco in zip(lista_Ap, lista_Area, lista_Preco):
    preco_por_m2 = preco / area
    preco_por_area.append((ap, preco_por_m2))

for ap, valor in preco_por_area:
    print(f"apartamneto {ap} : {valor:.2} por metro quadrado")

compra = min(preco_por_area, key = lambda x: x[1])
print(f"voce deve comprar a {compra}")



#estudar mais a fundo... 