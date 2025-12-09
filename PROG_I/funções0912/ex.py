def calcular_soma(min, max, inc):
    soma = 0 
    for i in range(min, max, inc):
        soma = soma + 1
    return soma


print(calcular_soma(0, 4, 1))
