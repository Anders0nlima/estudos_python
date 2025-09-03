lista = []
cont_par = 0
cont_impar = 0


for i in range(8):
    num = int(input(f"{i+1} - Digite: "))
    lista.append(num)
    if num % 2 == 0:
      cont_par += 1
    else:
      cont_impar += 1

print(lista)

print(f"A quantidade de numeros pares na lista é: {cont_par}")
print(f"A quantidade de numeros impares na lista é: {cont_impar}")
soma = sum(lista)
print(f"A soma de todos dos numeros da lista é: {soma}")