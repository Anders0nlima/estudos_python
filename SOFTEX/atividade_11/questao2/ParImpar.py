class ParImpar:
    def __init__(self, numero):
        self.numero = numero
        self.classificacao = self.definir_classificacao()
    
    def definir_classificacao(self):
        if(self.numero%2 == 0):
            return "Par"
        else:
            return "Impar"
        
 
