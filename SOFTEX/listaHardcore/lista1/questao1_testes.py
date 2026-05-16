""" 
1. Compressão de Lista (Run-Length Encoding)

Descrição:
Dada uma lista de caracteres, comprima-a substituindo sequências repetidas pelo caractere e a contagem.
Exemplo:
Entrada: ['a','a','b','b','b','c']
Saída: ['a','2','b','3','c']
Desafio extra: fazer in-place, sem usar lista auxiliar. 

"""

entrada = ['a','a','b','b','b','c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
saida = []  
cont = 1


for i in range(1, len(entrada)):
    if entrada[i] == entrada[i-1]:
        cont += 1
    else:
        saida.append(entrada[i-1])
        if cont > 1:
            saida.append(str(cont))
        cont = 1

saida.append(entrada[-1])
if cont > 1:
    saida.append(str(cont))
    cont = 1

print(saida)