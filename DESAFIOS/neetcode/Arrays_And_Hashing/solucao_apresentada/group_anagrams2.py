from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))

""" 
res = defaultdict(list) -> criar um dicionario especial, em que cria uma lista vazia ao acessar uma chave que ainda nao existe  

d = {}   #dicioario
d["a"].append(1) #quero acicionar o "a" 

isso nao vai funcionar, devemos fazer com defautdict(list)

from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)   # Funciona, por que ele criou uma automaticamente

print(d)

res = defaultdict(list) -> crie um dicionário onde cada nova chave começa automaticamente com uma lista vazia. 

"""