num1 = int(input("Nota1: "))
num2 = int(input("Nota2: "))
num3 = int(input("Nota3: "))


media = (num1*2 + num2*3 + num3*5)/(2+3+5)

if media >= 7:
    print("Aluno Aprovado")
elif media >= 5 or media <= 6.9:
    print("Em Exame")
else: 
    print("Reprovado")

print(media)