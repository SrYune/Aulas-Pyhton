#Entrada
import os
os.system("cls")
import time

num=int(input("Insira um número:"))
#Processamento
for i in range(0, num, 3):
    print(f"Múltiplos de 3={i}")
    time.sleep(4)
#Saída
print("Aperte Enter para finalizar")