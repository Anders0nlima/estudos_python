import math

class LojaTintas:
    def __init__(self, area):
        self.area = area
        self.litros_necessarios = self.calcular_litros()
        self.latas = self.calcular_latas()
        self.preco_total = self.calcular_preco()

    def calcular_litros(self):
        return self.area / 3

    def calcular_latas(self):
        return math.ceil(self.litros_necessarios / 18)

    def calcular_preco(self):
        return self.latas * 80