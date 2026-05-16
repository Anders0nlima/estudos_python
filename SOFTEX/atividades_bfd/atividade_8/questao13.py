v1 = int(input("Reta 1: "))
v2 = int(input("Reta 2: "))
v3 = int(input("Reta 3: "))

def eTriangulo(v1, v2, v3):
    if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v2 + v1:
        print("As retas fornecidas podem  forma um triangulo")
    else:
        print("Não podem forma um triangulo")
        
eTriangulo(v1, v2, v3)