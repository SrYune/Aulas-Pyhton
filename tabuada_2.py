#Entrada
import os
os.system("cls)")
import time

num=float(input("Insira o número desejado:"))
i=1

#Processamento
while i<=20:
    print(f'{num} x {i} = {num*i}')
    i= i+1 # incremento
    time.sleep(2)
    
#Saída
print("Aperte Enter para finalizar")