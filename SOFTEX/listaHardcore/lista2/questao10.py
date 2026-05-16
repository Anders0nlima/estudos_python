#10. Sorteio de Números Únicos
from random import randint

tamanho = int(input("tamanho: "))

for i in range(tamanho):
    print(randint(1, 60))