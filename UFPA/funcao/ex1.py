def soma(a,b):
    c = a + b
    return c

res1 = soma(10, 4)
print(res1)



def soma(*parametros):
    soma = 0
    for valor in parametros:
        soma += valor
    return soma
rest1 = soma(1, 2, 3, 4, 5, 6, 7, 8, 9)
rest2 = soma(10, 23, 15)
rest3 = soma(90, 180, 205)
print(rest1)
print(rest2)
print(rest3)



def par_ou_impar(valor):
    if (valor%2 == 0):
        return "valor é par"
    else:
        return "valor é impar"
    
result = par_ou_impar(8)
print(result)


L = [1, 2, 3]

print(max(L))
print(min(L))
print(sum(L))

