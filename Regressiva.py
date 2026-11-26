#Entrada
import os
os.system("cls")
import time

num=int(input("Insira um número:"))

#Processamento
while num>=0:
    print(f'{num} - 1 = {num-1}')
    num=num-1
    time.sleep(2)
    
#Saída
print("Aperte Enter para finalizar")