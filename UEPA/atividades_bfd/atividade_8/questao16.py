import random

def jogo(opcoes, opcao_jogo):
  if(opcao_jogo not in ["1", "2", "3"]):
      print("opção na valida")
  else:
      comp = random.choice(opcoes)
      jodador = opcoes[int(opcao_jogo) - 1] #transfoam em palavra
      print("computador: ", comp)
      print("sua escolha: ", jodador)
    
      if comp == jodador:
          print("empate")
      elif (jodador == "pedra" and comp == "tesoura") or (jodador == "papel" and comp == "pedra") or (jodador == "tesoura" and comp == "papel"):
          print("Você ganhou")
      else:
          print("Você perdeu")

opcoes = ["pedra", "papel", "tesoura"]
opcao_jogo = input("escolha entre [1-pedra], [2-papel] e [3-tesoura]: ")

jogo(opcoes, opcao_jogo)