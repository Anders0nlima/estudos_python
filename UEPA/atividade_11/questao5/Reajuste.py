class Reajuste:
    def __init__(self, salario_original):
        self.salario_original = salario_original
        self.percentual = self.definir_percentual()
        self.valor_aumento = self.calcular_aumento()
        self.salario_final = self.calcular_salario_final()

    def definir_percentual(self):
        if self.salario_original <= 1500:
            return 15
        else:
            return 10

    def calcular_aumento(self):
        return self.salario_original * (self.percentual / 100)

    def calcular_salario_final(self):
        return self.salario_original + self.valor_aumento