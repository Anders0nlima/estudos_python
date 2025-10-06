""" 
1. Compressão de Lista (Run-Length Encoding)

Descrição:
Dada uma lista de caracteres, comprima-a substituindo sequências repetidas pelo caractere e a contagem.
Exemplo:
Entrada: ['a','a','b','b','b','c']
Saída: ['a','2','b','3','c']
Desafio extra: fazer in-place, sem usar lista auxiliar. 

"""

entrada = ['a','a','b','b','b','c']
saida = [] # onde eu vou armazena a saida
cont = 1 

for i in range(1, len(entrada)):# range(inicio, fim)
    if entrada[i] == entrada[i-1]:
        cont += 1 
    else:
        saida.append(entrada[i-1])
        if cont > 1:
            saida.append(str(cont))
        cont = 1

saida.append(entrada[-1]) # -> 'c'
if cont > 1:
    saida.append(str(cont))

print(saida)


#nota importante: ao colocar 1 no inicio do range, impedimos que que o i em (i - 1) se transformace em -1 (index do ultimo elemento da lista) entao nao comparariamos o o elemento atual com o ultimo (o que veio antes dele) mas sim o o ultimo da lista.

#linha 26 saida.append(entrada[-1]): a ultima comparação feita e entre c e b porem o ultimo caractere nao foi comparado com ninguem pois a lista ja acabou, por isso temos que adciona manualmente
   
