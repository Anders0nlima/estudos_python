class TrianguloValido:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        self.tipo = self.classificar_triangulo()
    
    def eh_triangulo(self):
        return (
            self.lado_a + self.lado_b > self.lado_c and
            self.lado_a + self.lado_c > self.lado_b and
            self.lado_b + self.lado_c > self.lado_a
        )
    
    def classificar_triangulo(self):
        if not self.eh_triangulo():
            return "Não é um triângulo"

        if self.lado_a == self.lado_b == self.lado_c:
            return "Equilátero"
        elif (
            self.lado_a == self.lado_b or
            self.lado_a == self.lado_c or
            self.lado_b == self.lado_c
        ):
            return "Isósceles"
        else:
            return "Escaleno"
