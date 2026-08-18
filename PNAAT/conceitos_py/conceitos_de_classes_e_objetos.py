# parte 7

"""
Programação Orientada a Objetos (POO)
objeto possui:
- propriedades (ou atributos) -> que representam suas características ou estado
- comportamentos (ou métodos) -> que são as ações que esse objeto pode executar.

Os atributos são geralmente definidos dentro de um método especial chamado __init__, que funciona como o "construtor" do objeto. É ele quem "monta" o objeto e define seus atributos iniciais.

self é uma referência ao próprio objeto (à própria instância). É como o objeto se refere a si mesmo. Quando dizemos self.id_robo = "R-001", estamos dizendo: "Neste objeto específico que estou criando, guarde a informação "R-001" no meu atributo id_robo."
"""


"""
Propriedades e Comportamentos de Objetos
"""

class RoboIndustrial:
    # O método construtor que define os atributos iniciais
    def __init__(self, id_robo, ferramenta_inicial):
        # Atributos (Propriedades) do objeto
        self.id_robo = id_robo
        self.ferramenta_atual = ferramenta_inicial
        self.status = "em espera" # Um status padrão

    # Método (Comportamento) para mudar o status
    def ativar(self):
        print(f"Robô {self.id_robo} ativando...")
        self.status = "ativo" # O método altera o próprio atributo do objeto

    # Método para trocar a ferramenta
    def trocar_ferramenta(self, nova_ferramenta):
        self.ferramenta_atual = nova_ferramenta
        print(f"Robô {self.id_robo} trocou para a ferramenta: {self.ferramenta_atual}")

# Criando duas instâncias (objetos) da classe RoboIndustrial
robo_A = RoboIndustrial("R-A01", "garra")
robo_B = RoboIndustrial("R-B02", "soldador")

# Verificando os atributos iniciais de cada um
print(f"Status inicial do {robo_A.id_robo}: {robo_A.status}")
print(f"Status inicial do {robo_B.id_robo}: {robo_B.status}")

# Agora, vamos fazer o robo_A realizar uma ação
robo_A.ativar()

# Verificando os status novamente
print(f"Novo status do {robo_A.id_robo}: {robo_A.status}")
print(f"Status do {robo_B.id_robo} (não foi alterado): {robo_B.status}")

print("----------------------------------------------------------")

"""
Interagindo com Atributos e Métodos
"""

# 1- Ler e Modificar Atributos
print("=== parte 1 ===")
class SensorVibracao:
    def __init__(self, id_sensor):
        self.id_sensor = id_sensor
        self.vibracao_atual = 2.3  # em mm/s RMS
        self.limite_maximo = 4.5  # em mm/s RMS

# Criamos uma instância do sensor
sensor_vibracao = SensorVibracao("SENSOR-MOTOR-01")

# 1. ACESSANDO um atributo para verificar a vibração atual
print(f"Vibração atual: {sensor_vibracao.vibracao_atual} mm/s")

# 2. MODIFICANDO um atributo para definir um novo limite
print("Ajustando limite máximo de vibração...")
sensor_vibracao.limite_maximo = 5.0

# 3. VERIFICANDO a mudança
print(f"Novo limite máximo: {sensor_vibracao.limite_maximo} mm/s")

print("=== parte 2 ===")
# 2- Chamar Métodos

class Esteira:
    def __init__(self, id_esteira):
        self.id = id_esteira
        self.status = "parada" # Status inicial

    def ligar(self):
        self.status = "movendo"
        print(f"Esteira {self.id}: movendo.")

    def parar(self):
        self.status = "parada"
        print(f"Esteira {self.id}: parada para acesso do robô.")

class Robo:
    def __init__(self, id_robo):
        self.id = id_robo
        self.status = "em espera"

    def pegar_peca(self, esteira_alvo):
        print(f"Robô {self.id}: iniciando operação de coleta.")
        self.status = "trabalhando"

        # INTERAÇÃO: O robô ACESSA o atributo da esteira
        if esteira_alvo.status == "movendo":
            print(f"Robô {self.id}: a esteira está movendo. Solicitando parada...")
            # INTERAÇÃO: O robô CHAMA o método da esteira
            esteira_alvo.parar()

        print(f"Robô {self.id}: pegando a peça da esteira {esteira_alvo.id}.")
        # Lógica para pegar a peça aqui...
        print(f"Robô {self.id}: peça coletada com sucesso.")
        self.status = "em espera"

esteira_producao = Esteira("EST-01")
robo_braco = Robo("RB-01")

# 1. Ligamos a esteira
esteira_producao.ligar()

# 2. O robô tenta pegar a peça, interagindo com a esteira
robo_braco.pegar_peca(esteira_producao)

# 3. Verificamos o estado final da esteira
print(f"Estado final da esteira {esteira_producao.id}: {esteira_producao.status}")

print("----------------------------------------------")
"""
Criando uma nova classe e instanciando um objeto

obs: Em qualquer planta industrial (química, de tratamento de água, de alimentos), o controle preciso de fluxo de líquidos ou gases é essencial. Isso é feito por válvulas de controle. Uma válvula não é apenas "aberta" ou "fechada"; uma válvula proporcional pode ser, por exemplo, "37% aberta".
Nosso desafio é criar um "gêmeo digital" dessa válvula. Precisamos de um modelo em software (uma classe) que contenha suas informações essenciais (ID, tipo de fluido, abertura atual) e possa realizar suas ações fundamentais (ajustar a abertura, relatar seu estado). Criar esta classe é o primeiro passo para construir um sistema SCADA ou um painel de controle virtual.
"""

print("=== Contexto Teórico: Modelando a Realidade para o Controle de Processos ===")
# Passo 1: A Palavra-Chave 'class' - O Início do Projeto
class ValvulaControle:
    """
    Esta classe modela uma Válvula de Controle Proporcional,
    um componente crucial em sistemas de automação industrial para
    regular o fluxo de fluidos.
    """

    # Passo 2: O Construtor '__init__' - A Linha de Montagem do Objeto
    def __init__(self, id_valvula, tipo_fluido):
        # Passo 3: Atributos - As Propriedades de Cada Válvula
        print(f"CRIANDO nova válvula com ID: {id_valvula}")
        self.id_valvula = id_valvula
        self.tipo_fluido = tipo_fluido
        self.abertura_percentual = 0.0
        self.status = "operacional"

    # Passo 4: Métodos - Os Comportamentos da Válvula
    def ajustar_abertura(self, percentual_desejado):
        """Ajusta a posição da válvula para um novo percentual."""
        if 0 <= percentual_desejado <= 100:
            self.abertura_percentual = float(percentual_desejado)
            print(f"[{self.id_valvula}] Abertura ajustada para {self.abertura_percentual}%.")
        else:
            print(f"[{self.id_valvula}] ERRO: Abertura deve ser entre 0 e 100.")

    def relatar_estado(self):
        """Retorna uma string formatada com o estado atual da válvula."""
        estado = (f"--- Relatório da Válvula {self.id_valvula} ---\n"
                  f"  Fluido: {self.tipo_fluido}\n"
                  f"  Abertura: {self.abertura_percentual}%\n"
                  f"  Status: {self.status}\n"
                  f"------------------------------------")
        return estado

# --- Fim do Projeto (Classe) ---

# Passo 5: Instanciação - Fabricando os Objetos
print("--- Iniciando sistema de controle de fluidos ---")
valvula_agua_tanque = ValvulaControle("V-101", "Água Resfriada")
valvula_ar_compressor = ValvulaControle("V-25A", "Ar Comprimido")
print("-" * 20)

# Passo 6: Utilização - Colocando os Objetos para Trabalhar
valvula_agua_tanque.ajustar_abertura(75.5)
valvula_ar_compressor.ajustar_abertura(100)
print("-" * 20)
print(valvula_agua_tanque.relatar_estado())
print(valvula_ar_compressor.relatar_estado())

# Tentando um ajuste inválido
valvula_agua_tanque.ajustar_abertura(110)