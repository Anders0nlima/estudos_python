print("Infome o complimento em metros dos lados do terreno: ")
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
l4 = float(input("Lado 4: "))


def pagamento(l1, l2, l3, l4):
    perimetroTotal = ((l1+l2+l3+l4)*4)
    pagar = ((86.90 * perimetroTotal)/100)
    return pagar


print(pagamento(l1, l2, l3, l4))
