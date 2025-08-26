#----------------------------------------------------------------------
#Questão 1

numero_email = input("Número do celular ou email:")
senha = input("Senha:")
nome = input("Nome completo:")
usuario = input("Nome do usuario:")


print("O Número de celular ou email fornecido foi: ", numero_email)
print("a senha digitada foi: ", senha)
print("o nome inserido foi: ", nome)
print("o nome do usuario digitado é: ", usuario)



#----------------------------------------------------------------------
#Questão 2


print("triangulo retangulo")
#A = (base x altura) / 2
base = int(input("Base: "))
altura = int(input("Altura: "))
area = (base * altura)/2
print("Area do triangulo retangulo: ", area)


print("circulo")
#A = π * r²
pi = 3.14
raio = int(input("Raio: "))
area = (pi * (raio**2))
print("Area do circulo: ", area)


print("quadrado")
#A = l * l
lado = int(input("Lado: "))
area = (lado * lado)
print("Area do quadrado: ", area)


print("retângulo")
#A = h * c
comprimento = int(input("Base: "))
altura = int(input("Altura: "))
area = (comprimento * altura)
print("Area do retângulo: ", area)


#----------------------------------------------------------------------
#Questão 3 


lista_mes = ["maio", "junho", "julho", "agosto", "setembro", "outubro"]
lista_media = [66, 64, 54, 46, 60, 64]

lista_media[4] = 15

print(lista_mes)
print(lista_media)

