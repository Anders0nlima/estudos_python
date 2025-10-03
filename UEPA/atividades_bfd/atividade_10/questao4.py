#listaNota = [2, 8, 10, 6]

#cont = 0

#soma = sum(listaNota)
#media = soma/len(listaNota)
#print(media)

#while cont < len(listaNota):
#    print("Nota",cont+1, ":", listaNota[cont])
#    cont = cont + 1

listaNota = []

for i in range(3):
    notas = int(input("Digite a nota: "))
    listaNota.append(notas)
    tamanho = len(listaNota)
    soma = sum(listaNota)
    media = soma/tamanho
print(media) 


