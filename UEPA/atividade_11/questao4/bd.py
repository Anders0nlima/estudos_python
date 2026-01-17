class Database:
    def __init__(self, conexao):
        self.conexao = conexao
    
    def salvar(self, validar_triangulo):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO TrianguloValido (lado_a, lado_b, lado_c, tipo)
        VALUES (%s, %s, %s, %s)
        """
      
        dados = (
         validar_triangulo.lado_a,
         validar_triangulo.lado_b,
         validar_triangulo.lado_c,
         validar_triangulo.tipo
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()