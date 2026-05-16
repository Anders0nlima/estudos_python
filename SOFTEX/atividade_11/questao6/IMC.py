class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = self.calcular_imc()
        self.categoria = self.classificar()

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def classificar(self):
        if self.imc < 18.5:
            return "Abaixo do peso"
        elif self.imc < 25:
            return "Peso normal"
        else:
            return "Sobrepeso"