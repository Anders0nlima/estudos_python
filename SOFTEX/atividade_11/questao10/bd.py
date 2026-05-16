class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, tinta):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO LojaTintas
        (area, litros_necessarios, latas, preco_total)
        VALUES (%s, %s, %s, %s)
        """

        dados = (
            tinta.area,
            tinta.litros_necessarios,
            tinta.latas,
            tinta.preco_total
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()