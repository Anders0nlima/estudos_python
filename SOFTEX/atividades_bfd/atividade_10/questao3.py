#cont = 0
#num = int(input("Digite um valor: "))

#while cont < num:
#    if cont%2 == 0:
#        print(cont)
#    cont = cont + 1

cont = 0
num = int(input("Digite um valor: "))

for i in range(num):
    if cont%2 == 0:
        print(i)
    cont = cont + 1
    