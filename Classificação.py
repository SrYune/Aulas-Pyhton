import os
os.system("cls")
 
nome = input("Digite o nome do cliente:")
total_compras = float(input("Digite o total gasto deste mês:R$"))
 
if total_compras >= 5000:
    print("Cliente Ouro")
 
elif total_compras >= 2000:
    print("Cliente Prata")
 
else:
    print("Cliente Bronze")