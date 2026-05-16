from datetime import datetime

class CategoriaNatacao:
    def __init__(self, ano_nascimento):
        self.ano_nascimento = ano_nascimento
        self.idade = self.calcular_idade()
        self.categoria = self.definir_categoria()

    def calcular_idade(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

    def definir_categoria(self):
        if self.idade <= 9:
            return "MIRIM"
        elif self.idade <= 14:
            return "INFANTIL"
        elif self.idade <= 19:
            return "JÚNIOR"
        elif self.idade <= 25:
            return "SÊNIOR"
        else:
            return "MASTER"