
print("Os numeros devem ser diferentes: ")
print(" ")

num1 = int(input("primeiro numero: "))
num2 = int(input("segundo numero: "))
num3 = int(input("terceiro numero: "))



if num1 != num2 != num3:
    if num1 < num2 and num1 < num3:
        if num2 < num3:
            #print(num1, num2, num3) 
            print(num3, num2, num1)
        else:
            #print(num1, num3, num2)
            print(num2, num3, num1)
    elif num2 < num1 and num2 < num3:
        if num1 < num3:
            #print(num2, num1, num3)
            print(num3, num1, num2)
        else:
            #print(num2, num3, num1)
            print(num1, num3, num2)
    else:
        if num1 < num2:
            #print(num3, num1, num2)
            print(num3, num1, num2)
        else:
            #print(num3, num2, num1)
            print(num3, num2, num1)    
else:
    print("os numeros devem ser diferentes")

