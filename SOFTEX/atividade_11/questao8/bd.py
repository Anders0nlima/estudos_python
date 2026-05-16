class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, emprestimo):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO Emprestimo
        (valor_casa, salario, anos, prestacao_mensal, resultado)
        VALUES (%s, %s, %s, %s, %s)
        """

        dados = (
            emprestimo.valor_casa,
            emprestimo.salario,
            emprestimo.anos,
            emprestimo.prestacao_mensal,
            emprestimo.resultado
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()