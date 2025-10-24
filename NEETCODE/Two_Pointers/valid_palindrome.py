
def isPalindrome(s):
    reverso = s[::-1].replace(" ", "").upper()
    texto_limpo = "".join(caractere for caractere in reverso if caractere.isalnum())

    if texto_limpo == texto_limpo[::-1]:
        return True
    else:
        return False


print(isPalindrome("tab a cat"))