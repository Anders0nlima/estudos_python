def anagrama(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(anagrama("racecar", "carrace"))
print(anagrama("jar", "jam"))