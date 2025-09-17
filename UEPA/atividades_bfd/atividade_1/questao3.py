lista_mes = ["maio", "junho", "julho", "agosto", "setembro", "outubro"]
lista_media = [66, 64, 54, 46, 60, 64]

print(lista_mes)
print(lista_media)

edicao = int(input("Quer mudar algum valor? [1-sim ou 2-não]"))
if edicao == 2:
    print("Lista final: ")
    print(lista_mes)
    print(lista_media)
elif edicao == 1:
    num = int(input("Digite a posição em que se encontra o valor que voce quer mudar: [sendo o primeiro como valor 1]:"))

    if num <= len(lista_media):
        mudanca = int(input("Qual valor você quer: "))
        lista_media[num - 1] = mudanca
        print(lista_media)
    else:
        print("valor não encontrado")

else: 
    print("Valor nao valido")
    