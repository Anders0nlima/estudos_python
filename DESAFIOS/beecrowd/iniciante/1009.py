nome = input()
salarioFixo = float(input())
vendas = float(input())
comissaoFixa = 0.15

comissao = (vendas * comissaoFixa) + salarioFixo

print(f"TOTAL = R$ {comissao:.2f}")