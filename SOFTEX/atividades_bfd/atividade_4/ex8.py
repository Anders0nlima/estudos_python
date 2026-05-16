import math

horas = 5
minutos = 12
total_min = horas * 60 + minutos

#A
horas_a = math.ceil(total_min/60) #arrendonda para cima
preco_a = horas_a * 6

#B
if total_min <= 120:
    preco_b = 6
else:
    horas_extra = math.ceil((total_min - 120) / 60)
    preco_b = 6 + horas_extra * 3

#C
if total_min <= 15:
    preco_c = 0
else:
    horas_c = math.ceil((total_min - 15) / 60)
    preco_c = horas_c * 6


#D
if total_min <= 120 + 15:  # até 2h15min = só 6 reais
    preco_d = 6
else:
    horas_extra_d = math.ceil((total_min - (120 + 15)) / 60)
    preco_d = 6 + horas_extra_d * 3

#E
preco_e = total_min * 0.10

precos = {
    "A": preco_a,
    "B": preco_b,
    "C": preco_c,
    "D": preco_d,
    "E": preco_e
}









for est, preco in precos.items():
    print(f"Estacionamentos {est}: R$ {preco:.2f}") #Isso é o mesmo conceito de listas de tuplas, mas aplicado a dicionários, feitos na 7 e 5

melhor = min(precos, key=precos.get)
print(f"\nO estacionamento mais barato é o {melhor}, com valor R$ {precos[melhor]:.2f}")

#O argumento key=precos.get diz ao Python:
#“Quando for comparar as chaves (‘A’, ‘B’, …), use o valor de cada chave (o preço) pra decidir o menor.”
#precos.get("A") → 36.0