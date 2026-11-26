import os
import time
import random 

os.system("cls")

teste = [67, 42 , "Escola"]

print(teste[0])
print(teste[1])
print(teste[2])

#Testar insert
teste.insert(1, "Item") #Coloca "Item" na posição
print("Após insert 1" , teste[1])

#testar append
teste.append("Carlos") #Coloca no final
print("Após Append" , teste)

#modifica elementos
teste[0] = "Eduardo" #Modifica o elemento na posição especifica
print("Após modificação" , teste)

#del
del teste[2]#Apaga elemento
print("Após del", teste)

#remove
teste.remove("Escola")#Remove elementos
print("Após remove", teste)

#pop
removido = teste.pop(2)
print(f"Após pop (removido '{removido}'):", teste)