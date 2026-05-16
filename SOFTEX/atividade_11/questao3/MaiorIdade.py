class MaiorIdade:
    def __init__(self, idade):
        self.idade = idade
        self.acesso = self.definir_acesso()
    
    def definir_acesso(self):
        if(self.idade >= 18):
            return "Acesso Permitido"
        else:
            return "Acesso Negado"
        