# parte 4

"""
lista usa [] -> posso mudar
tupla usa () -> nao posso mudar é fixo
"""

temperaturas_celsius = [25.1, 25.5, 24.9, 26.0, 25.8]
print(f"Leituras iniciais de temperatura: {temperaturas_celsius}")

#create
temperaturas_celsius.append(26.2)
temperaturas_celsius.append(25.7)
print(f"Leituras após novas coletas: {temperaturas_celsius}")

#read
primeira_leitura = temperaturas_celsius[0] # Acessando o primeiro elemento
ultima_leitura = temperaturas_celsius[-1]  # Acessando o último elemento
print(f"Primeira leitura registrada: {primeira_leitura}°C")
print(f"Última leitura registrada: {ultima_leitura}°C")

#update
temperaturas_celsius[2] = 25.0  # Supondo que a terceira leitura (índice 2) foi corrigida
print(f"Leituras após correção: {temperaturas_celsius}")

#remove
temperaturas_celsius.pop(0)  # Remove o primeiro elemento (leitura mais antiga)
print(f"Leituras após remover a mais antiga: {temperaturas_celsius}")

#tamanho da lista
print(f"Número total de leituras registradas: {len(temperaturas_celsius)}")

#verificação
if 26.2 in temperaturas_celsius:
    print("A temperatura de 26.2°C foi registrada.")


temperaturas_celsius.sort()
print(f"Leituras ordenadas: {temperaturas_celsius}")  


"""
======= dicionairo =======

sensor = { "id" : 101,
           "tipo": True,
           "tamanho": 30
}

"""

estados_maquinas = {
    "maquina_1": "operacional", 
    "maquina_2": "manutencao", 
    "maquina_3": "parada", 
    "maquina_4": "operacional"
}

#create
estados_maquinas.update({"maquina_5": "operacional"})
estados_maquinas.update({"maquina_6": "manutencao"})
print(f"Estados após adicionar novas máquinas: {estados_maquinas}")

#read
estado_maquina_1 = estados_maquinas["maquina_1"]
estado_maquina_3 = estados_maquinas["maquina_3"]
print(f"O estado da máquina 1 é: {estado_maquina_1}")
print(f"O estado da máquina 3 é: {estado_maquina_3}")

#updade
estados_maquinas["maquina_2"] = "operacional"  # Supondo que a máquina 2 voltou a operar
print(f"Estados após atualização: {estados_maquinas}")

#delete
del estados_maquinas["maquina_3"]  # Remove o estado da máquina 3 (desativada)
print(f"Estados após remover uma máquina: {estados_maquinas}")


#tamanho
print(f"Número total de estados registrados: {len(estados_maquinas)}")

#listando todas
print(f"Máquinas atualmente registradas: {estados_maquinas.keys()}")



comandos_maquinas = {
    "maquina_A": ["ligar", "monitorar", "desligar"], 
    "maquina_B": ["manutencao", "calibrar"], 
    "maquina_C": ["ligar", "monitorar"], 
    "maquina_D": ["ligar", "desligar"]
}


print(f"\nComandos para as máquinas: {comandos_maquinas}")

proximo_comando = comandos_maquinas["maquina_A"].pop(0)
print(f"Executando comando: {proximo_comando} para a máquina A")
print(f"Comandos restantes para a máquina A: {comandos_maquinas['maquina_A']}")