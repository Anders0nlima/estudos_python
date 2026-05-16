#função sempre em cima(modelo)

def alturaT(area, baseT):
    h = ((2 * area)/baseT)
    return h

def areaQuadrado(alturaQ):
    areaQ = alturaQ * alturaQ
    return areaQ

area = int(input("area do trangulo: "))
baseT = int(input("base do trangulo: "))

alturaQ = (alturaT(area, baseT))

print(areaQuadrado(alturaQ))


