import os

os.system("cls")

#Entrada
peso = float(input("Insira seu peso:"))
altura = float(input("Insira sua altura:"))
imc = peso / (altura ** 2)

#Processamento e Saída
 
if imc <=18.5:
    print ("Abaixo do peso. Seu IMC foi calculado por IMC = peso / altura²")
elif imc <=24.9:
    print ("Peso normal. Seu IMC foi calculado por IMC = peso / altura²")
elif imc <=29.9:
    print ("Sobrepeso. Seu IMC foi calculado por IMC = peso / altura²")
elif imc <=34.9:
    print ("Obesidade Grau 1. Seu IMC foi calculado por IMC = peso / altura²")
elif imc <=39.9:
    print ("Obesidade Grau 2. Seu IMC foi calculado por IMC = peso / altura²")
else:
    print ("Obesidade Grau 3. Seu IMC foi calculado por IMC = peso / altura²")