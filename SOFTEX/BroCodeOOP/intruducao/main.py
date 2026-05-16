from car import Car

car1 = Car("Ferrari", 2024, "Red", True)
car2 = Car("Fusca", 1960, "White", False)
car3 = Car("Mustengue", 2010, "Black", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2.Drive()
car2.Stop()
