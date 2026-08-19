codigoA, unidadesA, valorA = input().split()
codigoB, unidadesB, valorB = input().split()

codigoA = int(codigoA)
unidadesA = int(unidadesA)
valorA = float(valorA)

codigoB = int(codigoB)
unidadesB = int(unidadesB)
valorB = float(valorB)

TOTAL = ((unidadesA*valorA)+(unidadesB*valorB))

print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")