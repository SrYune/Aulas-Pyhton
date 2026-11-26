#Entrada
import os
os.system("cls")
import time

num=int(input("Insira um número:"))

#Processamento
for i in range(0, num, 5):
    print(f"Contagem de 5={i}")
    time.sleep(4)
#Saída
print("Aperte Enter para finalizar")