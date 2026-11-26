import os

os.system("cls")

#Entrada
numero = float(input("Insira número desejado:"))

#Processamento
if numero >=1:
    print("Número positivo")
elif numero <=-1:
    print("Número negativo")
else:
    print("Número nulo, 0")