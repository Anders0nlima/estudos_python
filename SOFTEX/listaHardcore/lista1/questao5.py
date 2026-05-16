""" 
5. Contar Palavras Únicas (com import string)

Descrição:
Crie uma função que conte o número de palavras únicas em uma string, ignorando pontuação e maiúsculas/minúsculas.
Use:

import string


Exemplo:
Entrada: "Olá, olá! Mundo... mundo?"
Saída: 2 ('olá' e 'mundo') 

"""


import string

def frase_unica(frase):
    frase = frase.lower()

    for pontuacao in string.punctuation:
        frase = frase.replace(pontuacao, "")

    palavras = frase.split()

    unicas = []


    for palavra in palavras:
        if palavra not in unicas:
            unicas.append(palavra)
    
    return len(unicas), unicas

frase = "Olá, olá! Mundo... mundo?"
quantidade, lista_unicas = frase_unica(frase)

print("Palavras únicas:", lista_unicas)
print("Quantidade:", quantidade)




