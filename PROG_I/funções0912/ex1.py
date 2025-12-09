#5.12.1-Faça uma função em Python que receberá três notas de um aluno e calculará a
#média e verifique se o aluno foi aprovado por média, essa situação acontecerá toda vez
#que a m´deia for maior ou igual a 8.0.

def media(a, b, c):
    soma = a + b + c
    media = soma/3

    if media >= 8:
        return f"Aprovaod | media -> {media}"
    else:
        return f"R | media -> {media}"


print(media(8, 9, 10))



