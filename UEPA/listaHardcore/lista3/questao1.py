#Cifra de César – Reversível

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

frase = input("frase: ").lower()
chave = int(input("chave: "))

frase_separada = list(frase)
frase_codificada = ""
frase_descodificada = ""


for i in range(len(frase_separada)):
    letras = frase_separada[i]
    indice = alfabeto.index(frase_separada[i]) 
    codigo = (indice + chave) % len(alfabeto)  #o len(alfabeto) faz a volta ex: z vira b se a chave for 2
    frase_codificada += (alfabeto[codigo]) 

    descodificar = (indice) % len(alfabeto)
    frase_descodificada += (alfabeto[descodificar]) 
    
print(f"frase com cifra de césar: {frase_codificada}")  
print(f"frase codificada: {frase_descodificada}")  




