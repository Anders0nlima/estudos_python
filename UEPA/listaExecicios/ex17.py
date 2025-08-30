import random

opcoes = ["pedra", "papel", "tesoura"]

opcao_jogo = input("escolha entre [1-pedra], [2-papel] e [3-tesoura]")


if(opcoes != opcoes):
    print("opção na valida")
else:
    print("")
    comp = random.choice(opcoes)
    print("computador: ", comp)
    print("sua escolha: ", opcao_jogo)
    
    if comp == opcao_jogo:
        print("empate")
    elif (comp == "pedra") and (opcao_jogo == "papel"):
        print("você ganhou")
    elif (comp == "pedra") and (opcao_jogo == "tesoura"):
        print("computador ganhou")
    elif (comp == "papel") and (opcao_jogo == "pedra"):
        print("computador ganhou")
    elif (comp == "papel") and (opcao_jogo == "tesoura"):
        print("você ganhou")
    elif (comp == "tesoura") and (opcao_jogo == "papel"):
        print("computador ganhou")
    elif (comp == "tesoura") and (opcao_jogo == "pedra"):
        print("voce ganhou")
    