import os

os.system("cls")

#Entrada
nome = input("Insira o nome do produto:")
quantidade = int(input("Insira a quantidade disponível no estoque:"))

#Processamento e Saída

if quantidade >=30:
    print("Estoque adequado")
elif quantidade >=10:
    print("Estoque baixo")
else:
    print("Estoque crítico")
