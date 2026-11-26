import os

os.system("cls")

print("Conversor de Temperatura")

# Entrada-Especificações
temperatura_celsius = float(input("Informe a temperatura atual : "))

VALOR_FATOR = 9
SEGUNDO_FATOR = 160
TERCEIRO_FATOR = 5

# Processamento-Equação (Utilizando a sua constante TERCEIRO_FATOR)
temperatura_fahrenheit = (VALOR_FATOR * temperatura_celsius + SEGUNDO_FATOR) / TERCEIRO_FATOR

# Saída-Resultado
print(f"A temperatura de {temperatura_celsius}°C em Fahrenheit fica cerca de {temperatura_fahrenheit}°F")
