A, B, C = input().split()


A = float(A)
B = float(B)
C = float(C)

lista = [A, B, C]
lista.sort(reverse=True)

A = lista[0]
B = lista[1]
C = lista[2]

descLista = [A, B, C]


if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or C == A:
        print("TRIANGULO ISOSCELES")