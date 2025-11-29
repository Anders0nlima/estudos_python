class Car():
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def Drive(self): #metodo
        print(f"You drive the {self.model}")
    
    def Stop(self): #metodo
        print(f"You stop the car {self.model}")