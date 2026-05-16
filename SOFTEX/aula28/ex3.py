
class Folha:
    def __init__(self, formato):
        self._formato_folha = formato
    
    @property
    def formato(self):
        return self._formato_folha
    
    @formato.setter
    def formato(self, valor):
        self._formato_folha = valor
    
folha = Folha("A4")
folha.formato = "A0"
print(folha.formato)