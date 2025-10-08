#Comparação de Palavras – Mais Vogais

vogais = ["a", "e", "i", "o", "u"]
frase = input("frase: ")

separada = frase.split()
print(separada)

for palavras in separada:
    cont = 0
    for letras in palavras:
        if letras.lower() in vogais:
            cont += 1
    print(cont)
        



