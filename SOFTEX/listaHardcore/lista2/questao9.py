#9. Lista de Palavras – Contagem de Vogais

cont = 0
vogal = "a", "e", "i", "o", "u"

print("Digite uma frase:")
frase = input("-> ").lower()

frase_separada = frase.split()
quant_de_palavras = len(frase_separada)
print(f"exitem {quant_de_palavras} palavras na frase.")

for letra in frase:
    if letra.startswith(vogal):
        cont += 1
print(f"existem {cont} vogais na frase.")

for i in range(1, len(frase_separada)):
    palavra_anterior = frase_separada[i - 1]
    palavra_atual = frase_separada[i]

    vogais_anterior = sum(1 for letra in palavra_anterior if letra in vogal)
    vogais_atual = sum(1 for letra in palavra_atual if letra in vogal)

    if vogais_atual > vogais_anterior:
        print(f'"{palavra_atual}" tem mais vogais que "{palavra_anterior}".')
    elif vogais_atual < vogais_anterior:
        print(f'"{palavra_anterior}" tem mais vogais que "{palavra_atual}".')
    else:
        print(f'"{palavra_atual}" e "{palavra_anterior}" têm a mesma quantidade de vogais.')

