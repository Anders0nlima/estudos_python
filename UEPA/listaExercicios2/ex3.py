lista_ingrad = ["xicara de farinha", "xicara de chocolate me pó", "xicara de açucar", "xicara de leite"]

lista_ingrad_quant = [9/4, 4/3, 1+3/4, 5/6]

ingredientes = list(zip(lista_ingrad_quant, lista_ingrad))

ingredientes.sort()

for quant, ing in ingredientes:
    print(f"{quant:.2} - {ing}")