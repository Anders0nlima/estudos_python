class Database:
    def __init__(self, conexao):
        self.conexao = conexao
    
    def salva(self, maior_idade):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO MaiorIdade (idade, acesso)
        VALUES (%s, %s)
        """
      
        dados = (
         maior_idade.idade,
         maior_idade.acesso
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()

