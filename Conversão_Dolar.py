import os

os.system("cls")

#Entrada
dolar = float(input("Insira a quantidade de dolares:"))
cotacao = float(input("Insira a cotaçao desejada:"))

#Processamento
total = dolar * cotacao

#Saída
print(f"Convertido em uma cotação de {cotacao}, com a quantidade de {dolar} dolares em reais, é de {total:.2f}R$")