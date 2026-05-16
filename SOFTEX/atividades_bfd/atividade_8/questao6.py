# area de um trapezio: A = (B + b) * h / 2
baseMaior = float(input("Base maior: "))
baseMenor = float(input("Base manor: "))
altura = float(input("Altura: "))


def trapezio(baseMaior, baseMenor, altura):
    return (((baseMaior + baseMenor) * altura)/2)

print("Area do trapezio: ")
print(trapezio(baseMaior, baseMenor, altura))

