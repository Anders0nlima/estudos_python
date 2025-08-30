num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))


if (num1 != num2) and (num1 != num3) and (num2 != num3):
    if num1 > num2 and num1 > num3:
        print("maior numero", num1)
    elif num2 > num1 and num2 > num3:
        print("maior numero", num2)
    else:
        print("maior numero", num3)
else:
    print("os numeros devem ser diferentes entre si")