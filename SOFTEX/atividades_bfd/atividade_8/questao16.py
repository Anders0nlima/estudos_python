import random

cont = 1

while cont == 1:
    jogador = input("escolha entre pedra, papel ou tesoura: ").lower()
    comp  = (random.choice(["pedra","papel","tesoura"])).lower()


    if jogador == "pedra" and comp == "papel" or jogador == "papel" and comp == "tesoura" or jogador == "tesoura" and comp == "pedra":
        print("computador ganhou")
    elif jogador == "pedra" and comp == "tesoura" or jogador == "papel" and comp == "pedra" or jogador == "tesoura" and comp == "papel":
        print("você ganhou")
    else:
        print("empatou")

    print(f"escolha do computador: {comp}")

    cont = int(input("deseja jogar de novo: 1-[sim] 2-[não]"))

print("voce saiu")