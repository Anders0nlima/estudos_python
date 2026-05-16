valor_pago = float(input("valor total das compras: "))

if valor_pago > 100.00:
    print("Opções de pagamento: ")
    print("1- A vista")
    print("2- Duas parcelas (sem juros)")
    print("3- Tres ate dez parcelas (juros de 3%)")
    opcao = int(input("opção: "))
    if opcao == 3:
        quant_parcelas = int(input("quantas pacelas: [entre 3 e 10]"))
        if quant_parcelas >= 3 and quant_parcelas <= 10:
            montante = valor_pago * (1 + 0.03)**quant_parcelas
            print("total a pagar: (com juros de 3%): ", montante)
        else:
            print("quantidades de parcelas invalidadas")
    else:
        if opcao == 1:
          desc = valor_pago * 0.9
          print("desconto de 10%: ", desc)
        elif opcao == 2:
          parc = valor_pago/2
          print("parcela de duas vezes sem juros: ", parc)
else:
    print("Opções de pagamento: ")
    print("1- A vista")
    print("2- Duas parcelas (sem juros)")
    opcao = input(int("opção: "))
    if opcao == 1:
        desc = valor_pago * 0.9
        print("desconto de 10%: ", desc)
    elif opcao == 2:
        parc = valor_pago/2
        print("parcela de duas vezes sem juros: ", parc)