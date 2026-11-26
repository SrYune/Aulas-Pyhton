import os

os.system("cls")

#Entrada
temperatura = float(input("Digite a temperatura em Celsius: "))

#Processamento
if temperatura >= 30.0:
    print("Está quente")
elif temperatura >= 20.0:
    print("Está agradável")
elif temperatura >= 10.0:
    print("Está frio")
else: 
    print("Você está cozinhado mano.")