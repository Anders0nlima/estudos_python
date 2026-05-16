class Emprestimo:
    def __init__(self, valor_casa, salario, anos):
        self.valor_casa = valor_casa
        self.salario = salario
        self.anos = anos
        self.prestacao_mensal = self.calcular_prestacao()
        self.resultado = self.verificar_aprovacao()

    def calcular_prestacao(self):
        return self.valor_casa / (self.anos * 12)

    def verificar_aprovacao(self):
        limite = self.salario * 0.30
        if self.prestacao_mensal <= limite:
            return "Empréstimo aprovado"
        else:
            return "Empréstimo negado"