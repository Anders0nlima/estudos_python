

# CANCELADA 

from typing import List

def encode_debug(strs: List[str]) -> str:
    if not strs:
        return ""
    
    sizes = []
    for s in strs:
        sizes.append(len(s))

    header = ""
    for sz in sizes:
        header += str(sz) + ","
    header += '#'

    body = ""
    for s in strs:
        body += s
    
    encoded = header + body
    return encoded

def decode_debug(s: str):
    if not s:
        print("Entrada vazia -> decode retorna []")
        return []

    print("\n=== Decodificando ===")
    print("String recebida:", s)

    # 1️⃣ Extrair o cabeçalho (antes do '#')
    sizes = []   # lista com os tamanhos das palavras
    i = 0
    while s[i] != '#':   # percorre até encontrar o '#'
        cur = ""
        while s[i] != ',':  # lê até a próxima vírgula
            cur += s[i]
            i += 1
        sizes.append(int(cur))  # converte "4" -> 4
        i += 1  # pula a vírgula
    print("1) Tamanhos extraídos:", sizes)

    # 2️⃣ Avançar o índice para o início do corpo
    i += 1
    body = s[i:]
    print("2) Corpo (restante da string):", body)

    # 3️⃣ Fatiar o corpo conforme os tamanhos
    res = []
    idx = 0
    for sz in sizes:
        word = body[idx: idx + sz]
        res.append(word)
        print(f"   Pegando {sz} chars → '{word}'")
        idx += sz
    print("3) Lista reconstruída:", res)
    return res

# Teste prático:
encoded = "4,4,4,3,#neetcodeloveyou"
decode_debug(encoded)

encoded2 = "2,3,1,3,#wesay:yes"
decode_debug(encoded2)

print(encode_debug(["neet","code","love","you"]))
print(decode_debug(["neet","code","love","you"]))