#12 por litro


#input tempo gasto
# input velocidade media 
# d = t*v
# litros = d / 12


tempo = int(input("Quanto tempo de viagem: "))
velociade = int(input("Qual a velociade media: "))

distancia = tempo * velociade

litros_usados = distancia / 12

print(f"Com velociade media de {velociade}, com o tempo de {tempo} e distancia percorrida de {distancia}, foram utilizados {litros_usados} litros na viagem")