import os

os.system("cls")

#Entrada

valor_compra = float(input("Insira o valor da compra R$:"))

#Processamento e Saída
if valor_compra >=300:
    print(f"O valor de sua compra não contém nenhum frete! O valor total de sua compra é R${valor_compra}.")
else:
    frete = valor_compra + 25
    print(f"O valor de sua compra possui um frete de R$25,00, seu valor total agora subiu para R${frete}.")