#i = 1

#while i <= 5:
    #print(i)
    #i += 1

i = 1
notas = []

while i <= 3:
    nota = int(input(f"Qual o nota da sua avaliação {i}:"))
    notas.append(nota)
    i += 1
soma_notas = sum(notas)
media = soma_notas / len(notas)

print(media)


