num = int(input("Digite um numero: "))

def imparPar(num):
    if num%2 == 0:
        print(f"O numero: {num} é par")
    else:
        print(f"O numero: {num} é impar")
        
imparPar(num)