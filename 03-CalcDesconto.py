import os
os.system("cls")

print("Super Calculadora Pro Max 67 Aura+Ego")

# Passo 1 - Entrada de Dados
nome_do_produto = input("Informe o nome do produto: ")
valor_produto = float(input("Informe o valor total do produto (ex: 150): "))
promocao = float(input("Informe a promoçâo que deseja calcular (ex: 20): "))

# Passo 2 - Processamento
# Divide a porcentagem e multiplica pelo valor total
resultado = valor_produto - (valor_produto * promocao)/100 

# Passo 3 - Saída
print("------------------------------------------------------------------------------------------------")
print(f"O {nome_do_produto} vale cerca de: {resultado}")

input("Por favor,pressione Enter para finalizar.")
