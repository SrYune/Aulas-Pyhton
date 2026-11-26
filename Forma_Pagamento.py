import os

os.system("cls")

#Entrada

valor_compra = float(input("Insira o valor da compra R$:"))
pagamento = input ("Insira a forma de pagamento:")

#Processamento e Saída
if pagamento == "Pix":
    total = valor_compra - (valor_compra * 0.10)
    print(f"o valor final será  R$ {total}. ")
elif pagamento == "Dinheiro":
    total = valor_compra - (valor_compra * 0.05)
    print (f"O valor final será R$ {total}.")
else:
    print (f"Sem desconto sobre o valor. Mantém o valor R$ {valor_compra}")