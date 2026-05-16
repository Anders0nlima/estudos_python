class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        return "Aprovado" if self.calcular_media() >= 7 else "Reprovado"