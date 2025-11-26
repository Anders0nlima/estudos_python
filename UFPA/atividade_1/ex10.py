def numero_por_extenso(n):
    unidades = [
        "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = [
        "dez", "onze", "doze", "treze", "catorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove"
    ]

    dezenas = [
        "", "", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"
    ]

    centenas = [
        "", "cento", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos", "oitocentos",
        "novecentos"
    ]

    # CASOS DIRETOS
    if n == 0:
        return ""
    if n == 100:
        return "cem"
    if n == 1000:
        return "mil"

    texto = ""

    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    # centenas
    if c > 0:
        texto += centenas[c]
        if n % 100 != 0:
            texto += " e "

    # 10–19
    if 10 <= n % 100 <= 19:
        texto += especiais[(n % 100) - 10]
        return texto

    # dezenas
    if d > 0:
        texto += dezenas[d]
        if u > 0:
            texto += " e "

    # unidades
    if u > 0:
        texto += unidades[u]

    return texto



total_letras = 0

for numero in range(1, 1001):
    palavra = numero_por_extenso(numero)
    palavra_sem_espacos = palavra.replace(" ", "").replace("-", "")
    total_letras += len(palavra_sem_espacos)

print("Total de letras usadas:", total_letras)