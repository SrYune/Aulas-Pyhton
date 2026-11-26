import os

os.system("cls")

print("Conversor de Temperatura")

# Entrada-Especificações
temperatura_fahrenheit = float(input("Informe a temperatura atual : "))

VALOR_FATOR = 9
SEGUNDO_FATOR = 32
TERCEIRO_FATOR = 5

# Processamento-Equação (Utilizando a sua constante TERCEIRO_FATOR)
temperatura_celsius = (temperatura_fahrenheit - SEGUNDO_FATOR)*TERCEIRO_FATOR/VALOR_FATOR

# Saída-Resultado
print(f"A temperatura de {temperatura_fahrenheit}°F em Celsius fica cerca de {temperatura_celsius}°C")