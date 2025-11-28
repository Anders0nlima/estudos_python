class Folha:
    def __init__(self, formato):
        self.formato = formato
    
    def get_formato(self):
        return self._formato_folha
    
folha = Folha("A4")
print(folha.formato)