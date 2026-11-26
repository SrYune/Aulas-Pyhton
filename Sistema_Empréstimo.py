import os
os.system("cls")

#Entrada
cliente = float(input("Insira seu salário:"))
valor_parcela = float(input("Insira o valor da parcela:"))

#Processamento e Saída
if cliente >valor_parcela:
   valor_parcela = cliente * 0.30
   print("Parcela negada")
else:
   print("Parcela aprovada")