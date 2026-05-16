estoque = {
"maca": 10,
"banana": 5,
"laranja": 8
}

estoque.update({"pera": 12})
del estoque["banana"]

print(estoque.keys())
