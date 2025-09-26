v1 = int(input("1- Valor: "))
v2 = int(input("2- Valor: "))
v3 = int(input("3- Valor: "))


def comparar(v1, v2, v3):
   if v1 >= v2 and v1 >= v3:
       return v1
   elif v2 >= v1 and v2 >= v3:
       return v2
   else:  
      return v3

print("O maior deles é: ")
print(comparar(v1, v2, v3))