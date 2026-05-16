# Usando um dicionário padrão:

palavras = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']

cont_dict = {}

for palavra in palavras:
    if palavra in cont_dict:
        cont_dict[palavra] += 1
    else: 
        cont_dict[palavra] = 1

print(cont_dict)

#------------------------------------------
# Usando defaultdict:

from collections import defaultdict

palavras_dicts = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']

cont_defautdict = defaultdict(int)

for palavra in palavras_dicts:
    cont_defautdict[palavra] += 1 

print(cont_defautdict)