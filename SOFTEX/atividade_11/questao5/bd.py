class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, reajuste):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO Reajuste
        (salario_original, percentual, valor_aumento, salario_final)
        VALUES (%s, %s, %s, %s)
        """

        dados = (
            reajuste.salario_original,
            reajuste.percentual,
            reajuste.valor_aumento,
            reajuste.salario_final
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()