from collections import defaultdict

def group_anagrams_count(strs):
    buckets = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        key = tuple(counts)
        buckets[key].append(s)
    return list(buckets.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams_count(strs))


# defaultdict -> cria automaticamente um valor padrão quando você acessa uma chave inexistente.

#estudar o que ta no chat a outra resoução