num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))
num3 = int(input("digite o terceiro valor: "))


if (num1 < num2 + num3) and (num2 < num1 + num3) and (num3 < num2 + num1):
    print("podem forma um triangulo")
else: 
    print("não podem forma um triangulo")
