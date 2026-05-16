import math

x1, y1 = map(float, input("digite as coordenadas de A (x, y):").split())
x2, y2 = map(float, input("digite as coordenadas de A (x, y):").split())
x3, y3 = map(float, input("digite as coordenadas de A (x, y):").split())



AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
CA= math.sqrt((x1 - x3)**2 + (y1 - y3)**2)


print(f"AB = {AB:.2f}")
print(f"BC = {BC:.2f}")
print(f"CA = {CA:.2f}")


""" 
COMO FUNCIONA:
x1, y1 = map(float, input("digite as coordenadas de A (x, y):").split()) 

1- input("digite as coordenadas de A (x, y) -> "2 5" (quando se digita 2 5 no terminal) e feito uma string 
2- "2 5".split() -> ["2", "5"] separa as strings
3- map(float, ...) map(float, ["2", "5"]) -> [2.0, 5.0] ate estao estavamos trabalhando com uma string, porem agora sao dois, ou seja, e necessario mapealas por isso o map() para conseguir ler as duas, o float elimina o formato de string, passado para o formato [2.0, 5.0] 
2- x1, y1 = ... nesse ponto ele desempacota em dois valores, sendo o primero 2.0(x1) e o segundo 5.0(y1)

"""