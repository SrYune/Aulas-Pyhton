#Entrada
import os
os.system("cls)")
import time

num=5
i=1

#Processamento
while i<=10:
    print(f'{num} x {i} = {num*i}')
    i= i+1 # incremento
    time.sleep(4)
    
#Saída
print("Aperte Enter para finalizar")