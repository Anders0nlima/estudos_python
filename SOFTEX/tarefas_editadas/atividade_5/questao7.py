listaAlfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

frase = input("Digite uma frase que queira decodificar: ")
chave = int(input("chave: "))

separar = list(frase)
print(separar)

cont = 0
while cont < (len(separar)):
    if separar[cont] not in listaAlfa:
        continue
    indice = listaAlfa.index(separar[cont])
    codigo = indice + chave

    indiceCodigo = listaAlfa[codigo]
    
    codificado = (list(indiceCodigo))

    fraseAjustada = " ".join(codificado)
    print(fraseAjustada)
    cont += 1