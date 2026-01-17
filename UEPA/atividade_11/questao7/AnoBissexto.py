class AnoBissexto:
    def __init__(self, ano):
        self.ano = ano
        self.resultado = self.verificar()

    def verificar(self):
        if (self.ano % 400 == 0) or (self.ano % 4 == 0 and self.ano % 100 != 0):
            return "Ano bissexto"
        else:
            return "Ano não bissexto"