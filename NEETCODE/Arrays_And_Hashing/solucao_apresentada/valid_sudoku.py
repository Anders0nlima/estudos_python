#parte cancelada/nao inteira ou errada - mas valida para estudos posteriores
matriz_9x9 = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]


for i in range(len(matriz_9x9)):
    linha_atual = matriz_9x9[i]

    numero_na_linha = [elemento for elemento in linha_atual if elemento != "."] #tiramos os "."
    conjuto_de_numeros = set(numero_na_linha) #tira de maneira automatica os duplicados

    print(f"Linha {i + 1}: {linha_atual}")

    if len(numero_na_linha) != len(conjuto_de_numeros): #
        print(f"  -> REPETIÇÃO ENCONTRADA! A linha tem números duplicados.")
    else:
        print(f"  -> OK. Não há repetição de números nesta linha.")
        print("-" * 30)

#coluna

colunas = list(zip(*matriz_9x9))
N = len(colunas)

for j in range(N):
    coluna_atual = colunas[j]

    numero_de_coluna = [elemento for elemento in coluna_atual if elemento != "."] 
    conjutos_de_numeros = set(numero_de_coluna)

    print(f"Coluna {j + 1}: {coluna_atual}")

    if len(numero_de_coluna) != len(conjuto_de_numeros):
        print(f" -> REPETIÇÃO ENCONTRADA! A linha tem números duplicados.")
    else:
        print(f" -> OK. Não há repetição de números nesta linha.")
        print("-" * 30)

bloco_id = 0

for linha_inicio in range(0, 9, 3):
    for coluna_inicio in range(0, 9, 3):
        bloco_id += 1
        elemento_do_bloco = []

        for i in range(3):
            for i in range(3):
                elemento = matriz_9x9[linha_inicio + i][coluna_inicio + i] 
                elemento_do_bloco.append(elemento)

                numeros_no_bloco = [e for e in elemento_do_bloco if e != "."]
                conjunto_de_numero = set(numeros_no_bloco)

                print(f"Bloco {bloco_id} (Começa em [{linha_inicio},{coluna_inicio}]): {numeros_no_bloco}")

                if len(numero_de_coluna) != len(conjunto_de_numero):
                    print(f"  -> REPETIÇÃO ENCONTRADA no Bloco {bloco_id}!")
                else:
                    print(f"  -> OK. Sem repetições neste bloco.")
                print("-" * 40)










""" from random import randint

N = 9

matriz_9x9 = [[0] * N for _ in range(N)]

for linha in matriz_9x9:
    print(linha) """
