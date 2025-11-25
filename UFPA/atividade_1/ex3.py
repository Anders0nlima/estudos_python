nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))


soma = ((nota1*1) + (nota2*1) + (nota3*2))
ponderada = 4

media = soma / ponderada

if media >= 60:
    print(f"Aprovado: media {media}")
else: 
    print(f"Reprovado: media {media}")