import os

os.system("cls")

#Entrada
nome_do_produto = input("Diga o nome do produto:")
valor_compra = float(input("Insira o valor da compra:"))


#Processamento e Saída
if valor_compra >=500:
    total = valor_compra - (valor_compra / 10)
    desconto = valor_compra / 10
    print("------------------------------------------------------------------------------------------------")
    print(f"O {nome_do_produto} vale cerca de: {total}R$, com o desconto de {desconto}R$ sendo seu valor original, {valor_compra}R$")


else:
    total = valor_compra
    print("------------------------------------------------------------------------------------------------")
    print(f"O {nome_do_produto} vale cerca de: {valor_compra}R$")

