lista_vogal = ["A", "E", "I", "O", "U"]

caractere = input("digite uma letra: ").upper()

if caractere in lista_vogal:
    print(f"A letra {caractere} é vogal")
else:
    print(f"A letra {caractere} é consoante")
