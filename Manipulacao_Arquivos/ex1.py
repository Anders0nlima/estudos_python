
caminho = "C:\Projetos\estudos_python\Manipulacao_Arquivos\msg.txt"

with open(caminho, "r") as arq:
    mensage = arq.read()

print(mensage)