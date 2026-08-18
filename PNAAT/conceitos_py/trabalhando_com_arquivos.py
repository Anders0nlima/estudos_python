# parte 8

"""
CSV, TXT e JSON
"""
# Exemplo de leitura de arquivos TXT, CSV e JSON em Python

# 1. Abrindo e lendo um arquivo TXT
with open('PNAAT/conceitos_py/dados_sensores.txt', 'r', encoding='utf-8') as arquivo_txt:
    conteudo_txt = arquivo_txt.read()
    print(conteudo_txt)
print("-" * 40)

# 2. Abrindo e lendo um arquivo CSV
import csv

print("Leitura de arquivo CSV:")
with open('PNAAT/conceitos_py/dados_sensores.csv', 'r', encoding='ISO-8859-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)
print("-" * 40)

# 3. Abrindo e lendo um arquivo JSON
import json

print("Leitura de arquivo JSON:")
with open('PNAAT/conceitos_py/dados_sensores.json', 'r', encoding='utf-8') as arquivo_json:
    dados_json = json.load(arquivo_json)
    print(dados_json)
print("-" * 40)



# Exemplo criando arquivos CSV e JSON

import csv
import json

# Simulação de leituras de temperatura
temperaturas = [22.5, 23.0, 22.8, 23.2, 22.9]

# 1. Gravar temperaturas em CSV
with open('temperaturas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Leitura', 'Temperatura'])
    for i, temp in enumerate(temperaturas, 1):
        writer.writerow([i, temp])

# 2. Criar lista de dicionários para JSON
dados_json = [{"Leitura": i+1, "Temperatura": temp} for i, temp in enumerate(temperaturas)]

# 3. Salvar dados em JSON
with open('relatorio.json', 'w', encoding='utf-8') as f:
    json.dump(dados_json, f, ensure_ascii=False, indent=2)





"""
Um dispositivo de borda (edge device), como um gateway de IoT em uma fábrica, não possui dados "hard-coded" (fixos no código). Ele precisa ser flexível. Ao ligar, ele executa uma rotina de inicialização:

- Lê um arquivo de configuração para saber a qual rede Wi-Fi se conectar e para qual servidor enviar dados.
- Lê um arquivo de log para verificar se houve falhas na última execução.
- Processa dados históricos de sensores para calibragem inicial.
"""

# Importando os módulos necessários para CSV e JSON
import csv
import json

# --- Cenário: Simulação de inicialização de um Gateway IoT ---

# Primeiro, vamos simular a existência dos arquivos que nosso programa irá ler.
# Em um cenário real, esses arquivos já estariam no dispositivo.

# Arquivo 1: device_id.txt (Texto Simples)
with open("device_id.txt", "w") as f:
    f.write("GW-I40-BR-031")

# Arquivo 2: sensor_log.csv (CSV)
with open("sensor_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "vibration_x", "vibration_y"])
    writer.writerow(["1678886400", "0.51", "1.20"])
    writer.writerow(["1678886401", "0.53", "1.22"])
    writer.writerow(["1678886402", "0.95", "1.89"]) # Anomalia

# Arquivo 3: config.json (JSON)
config_data = {
    "network": {
        "wifi_ssid": "FactoryFloor_Net",
        "wifi_pass": "senhaSuperSegura123"
    },
    "server": {
        "host": "data.minhafabrica.com",
        "port": 8883
    },
    "active_sensors": ["Temperature", "Vibration"]
}
with open("config.json", "w") as f:
    json.dump(config_data, f, indent=4)

print("--- Arquivos de simulação criados. Iniciando leitura. ---\n")

# 1. LENDO ARQUIVO DE TEXTO SIMPLES (.txt)
print("--- 1. Lendo ID do Dispositivo de 'device_id.txt' ---")
try:
    with open("device_id.txt", "r") as file:
        device_id = file.read().strip()
        print(f"ID do Gateway lido com sucesso: {device_id}\n")
except FileNotFoundError:
    print("ERRO: Arquivo de ID não encontrado!\n")

# 2. LENDO ARQUIVO CSV
print("--- 2. Processando Log de Sensor de 'sensor_log.csv' ---")
try:
    with open("sensor_log.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(f"Cabeçalho do CSV: {header}")
        for row in csv_reader:
            timestamp = int(row[0])
            vib_x = float(row[1])
            if vib_x > 0.9:
                print(f"ALERTA: Vibração anômala detectada no timestamp {timestamp}: {vib_x}")
    print("\n")
except FileNotFoundError:
    print("ERRO: Arquivo de log do sensor não encontrado!\n")

# 3. LENDO ARQUIVO JSON
print("--- 3. Carregando Configurações de 'config.json' ---")
try:
    with open("config.json", "r") as file:
        config = json.load(file)
        server_host = config["server"]["host"]
        active_sensors = config["active_sensors"]
        print(f"Gateway configurado para enviar dados para: {server_host}")
        print(f"Sensores ativos na configuração: {active_sensors}\n")
except FileNotFoundError:
    print("ERRO: Arquivo de configuração não encontrado!\n")
except json.JSONDecodeError:
    print("ERRO: O arquivo de configuração está mal formatado (não é um JSON válido)!\n")



"""
Sistemas industriais geram um volume massivo de dados. A capacidade de salvar esses dados de forma estruturada e eficiente é vital para:

- Rastreabilidade (Traceability): Salvar o log de cada etapa do processo de produção de um lote. Se um problema de qualidade for detectado, é possível rastrear exatamente o que aconteceu.
- Manutenção Preditiva: Registrar continuamente dados de sensores (vibração, temperatura). Esses dados históricos são a matéria-prima para modelos de IA que preveem falhas de máquinas.
- Auditoria e Conformidade: Gerar relatórios imutáveis que provam que um processo foi executado dentro dos parâmetros de segurança e qualidade exigidos.

Dominar a escrita de arquivos permite que seus programas deixem um "rastro digital" confiável das operações do sistema.
"""


# Importando os módulos necessários
import csv
import json
from datetime import datetime

# --- Cenário: Simulação de um ciclo de operação em uma célula de manufatura ---

# 1. ESCREVENDO EM ARQUIVO DE TEXTO (.txt) - MODO 'w' (Write)
print("--- 1. Iniciando novo log de ciclo de produção ---")
with open("ciclo_log.txt", "w") as log_file:
    timestamp_inicio = datetime.now().isoformat()
    log_file.write(f"Ciclo de produção iniciado em: {timestamp_inicio}\n")
    log_file.write("Status: Célula de montagem energizada.\n")

print("Log inicial 'ciclo_log.txt' criado/sobrescrito.\n")

# 2. ADICIONANDO DADOS A UM ARQUIVO CSV - MODO 'a' (Append)
print("--- 2. Coletando e salvando dados de sensores em 'dados_sensor.csv' ---")
leituras_sensor = [
    {"temp": 45.2, "pressao": 1015},
    {"temp": 47.8, "pressao": 1012},
    {"temp": 49.1, "pressao": 1010}
]

with open("dados_sensor.csv", "a", newline="") as csv_file:
    fieldnames = ["timestamp", "temperatura_c", "pressao_mbar"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    for leitura in leituras_sensor:
        timestamp_leitura = datetime.now().isoformat()
        writer.writerow({
            "timestamp": timestamp_leitura,
            "temperatura_c": leitura["temp"],
            "pressao_mbar": leitura["pressao"]
        })
print("Novas leituras de sensor adicionadas a 'dados_sensor.csv'.\n")

# 3. SALVANDO ESTADO FINAL EM ARQUIVO JSON
print("--- 3. Salvando estado final da máquina em 'estado_final.json' ---")
estado_maquina = {
    "id_maquina": "MAQ-007",
    "timestamp_final": datetime.now().isoformat(),
    "ultimo_ciclo": {
        "id_lote": "LOTE-54B9",
        "pecas_produzidas": 1500,
        "pecas_rejeitadas": 3
    },
    "status_ferramentas": {
        "ferramenta_corte": "87% de vida útil",
        "ferramenta_solda": "calibrada"
    }
}

with open("estado_final.json", "w") as json_file:
    json.dump(estado_maquina, json_file, indent=4)

print("Estado final da máquina salvo em 'estado_final.json'.")