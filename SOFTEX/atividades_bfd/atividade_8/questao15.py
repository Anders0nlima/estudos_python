v1 = int(input("Reta 1: "))
v2 = int(input("Reta 2: "))
v3 = int(input("Reta 3: "))

def eTriangulo(v1, v2, v3):
    if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v2 + v1:
        if v1 == v2 == v3:
            print("triangulo equilatero")
        elif v1 != v2 != v3:
            print("triangulo escaleno") 
        else:
            print("triangulo isoceles")
    else:
        print("Não podem forma um triangulo")
        
eTriangulo(v1, v2, v3)