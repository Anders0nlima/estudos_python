
class Folha:
    def __init__(self, formato):
        self._formato = formato
    
    @property
    def formato(self):
        return self._formato
    
    
folha = Folha("A4")
print(folha.formato)