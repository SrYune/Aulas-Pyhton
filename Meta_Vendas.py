import os

os.system("cls")

#Entrada
nome = input("Digite seu nome:")
valor_total = float(input("Insira o valor de suas vendas totais esse mês R$:"))

#Processamento
if valor_total >=15000:
    print("Excelente!")
elif valor_total >=10000:
    print("Meta atingida!")
else:
    print("Meta não atingida...")