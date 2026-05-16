print("Informe os valores da função do segundo grau: ")
b = int(input("Valor de B: "))
a = int(input("Valor de A: "))
c = int(input("Valor de C: "))

delta = b**2 - 4 * a * c


print("Valor do delta: ", delta)

if delta == 0:
    print("Uma raiz real")
elif delta > 0:
    print("Duas raízes reais")
else: 
    print("Não tem solução nos reais")