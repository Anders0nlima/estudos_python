class triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tipo(self):
        if (self.a == self.b == self.c):
            print("Triengulo Equilatero")
        elif (self.a != self.b == self.c):
            print("Triangulo Isósceles")
        else:
            print("Triangulo Escaleno")


while True:
    print("Valores do Triangulo")

    lado_a = int(input("Lado A: "))
    lado_b = int(input("Lado B: "))
    lado_c = int(input("Lado C: "))
    

    if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
        #print("tringulo válido")
        valores = triangulo(lado_a, lado_b, lado_c)
        valores.tipo()

        sair = int(input("Digite 1 para continuar ou 0 para sair: "))
        if sair == 0:
            break
        else:
            continue
        
    else:
        print("O tringulo não é valido")
        print("Saindo...")
        break

    