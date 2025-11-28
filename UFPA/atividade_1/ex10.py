def numero_por_extenso(n): #numero entre 1 e 1000 por extenso
    unidades = [
        "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove" #0 a 9 (ignoro o zero)
    ]

    especiais = [ # 10 a 19
        "dez", "onze", "doze", "treze", "catorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove"
    ]

    dezenas = [ #20 a 90
        "", "", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa" 
    ]

    centenas = [ #100 a 900
        "", "cento", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos", "oitocentos",
        "novecentos"
    ]

    #sao as exeções
    if n == 0:
        return ""
    if n == 100:
        return "cem" 
    if n == 1000:
        return "mil"

    texto = ""
                         #351
    c = n // 100         #3
    d = (n % 100) // 10  #5
    u = n % 10           #1

    if c > 0:  #montei pra centena  "trezentos"
        texto += centenas[c]
        if n % 100 != 0:
            texto += " e " #so se tiver unidade

    if 10 <= n % 100 <= 19: #pra dezena "ciquenta"
        texto += especiais[(n % 100) - 10]
        return texto

    if d > 0:   #pra decimal "um", pra que fique trezentos e ciquenta e um
        texto += dezenas[d]
        if u > 0:
            texto += " e " 

    if u > 0:
        texto += unidades[u]

    return texto



total_letras = 0

for numero in range(1, 1001):
    palavra = numero_por_extenso(numero)
    palavra_sem_espacos = palavra.replace(" ", "").replace("-", "")
    total_letras += len(palavra_sem_espacos)

print("Total:", total_letras) #exsitem 19.662 letras entre 1 e 1000 quando é por extenso (sem espaços)