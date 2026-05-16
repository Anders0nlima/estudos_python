lista_ingrad = ["xicara de farinha", "xicara de chocolate me pó", "xicara de açucar", "xicara de leite"]

lista_ingrad_quant = [9/4, 4/3, 1+3/4, 5/6]


lista_junta = list(zip(lista_ingrad_quant, lista_ingrad))

lista_junta.sort()

for quant, ingre in lista_junta:
    print(f"{quant:.2} - {ingre}")
