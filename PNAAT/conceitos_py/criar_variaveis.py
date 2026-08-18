# parte 1 

# Conversão de string para inteiro
numero_str = "100"
numero_int = int(numero_str) # Converte a string "100" para um inteiro 100
print(numero_int) # Saída: 100

# Conversão de string para float
numero_str = "100.5"
numero_float = float(numero_str) # Converte a string "100.5" para um float 100.5
print(numero_float) # Saída: 100.5

# Conversão de inteiro para string
numero_int = 100
numero_str = str(numero_int) # Converte o inteiro 100 para uma string "100"
print(numero_str) # Saída: "100"

# Conversão de float para string
numero_float = 100.5
numero_str = str(numero_float) # Converte o float 100.5 para uma string "100.5"
print(numero_str) # Saída: "100.5"

# Conversão de inteiro para float
numero_int = 100
numero_float = float(numero_int) # Converte o inteiro 100 para um float 100.0
print(numero_float) # Saída: 100.0

# Conversão de float para inteiro
numero_float = 100.5
numero_int = int(numero_float) # Converte o float 100.5 para um inteiro 100 (truncando a parte decimal)
print(numero_int) # Saída: 100

# Conversão de string para booleano
boolean_str = "True"
boolean_val = bool(boolean_str) # Converte a string "True" para um booleano True
print(boolean_val) # Saída: True

# Conversão de inteiro para booleano
numero_int = 1
boolean_val = bool(numero_int) # Converte o inteiro 1 para um booleano True (0 seria False)
print(boolean_val) # Saída: True

# Conversão de float para booleano
numero_float = 0.0
boolean_val = bool(numero_float) # Converte o float 0.0 para um booleano False (qualquer valor diferente de 0 seria True)
print(boolean_val) # Saída: False

# Conversão de booleano para string
boolean_val = True
boolean_str = str(boolean_val) # Converte o booleano True para uma string "True"
print(boolean_str) # Saída: "True"