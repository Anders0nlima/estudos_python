#Usando um dicionário padrão

dados = [
    ('Matemática', 'Alice'),
    ('Matemática', 'Bob'),
    ('Inglês', 'Alice'),
    ('Ciência', 'Charlie'),
]

agrupado_dict = {}

for materia, nome in dados:
    if materia not in agrupado_dict:
        agrupado_dict[materia] = []
    agrupado_dict[materia].append(nome)
print(agrupado_dict)

#Usando defaultdict

from collections import defaultdict

dados = [
    ('Matemática', 'Alice'),
    ('Matemática', 'Bob'),
    ('Inglês', 'Alice'),
    ('Ciência', 'Charlie'),
]

agrupado_defautdict = defaultdict(list)

for materia, nome in dados:
    agrupado_defautdict[materia].append(nome)


print(agrupado_defautdict)