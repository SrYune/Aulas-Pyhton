import os

os.system("cls")

#Entrada
nome = input("Digite seu nome:")
valor_vendas = float(input("Insira o valor de suas vendas R$:"))

#Processamento e Saída

if valor_vendas >=20000:
    comissao = valor_vendas * 0.10
    print("------------------------------------------------------------------------------------------------")
    print(f"Vendendo um total de {valor_vendas}R$, com uma comissão de 10%, sua comissão é de {comissao} R$ ")
elif valor_vendas >=10000:
    comissao = valor_vendas * 0.07
    print("------------------------------------------------------------------------------------------------")
    print(f"Vendendo um total de {valor_vendas}R$, com uma comissão de 7%, sua comissão é de {comissao} R$ ")
else:
    comissao = valor_vendas * 0.05
    print("------------------------------------------------------------------------------------------------")
    print(f"Vendendo um total de {valor_vendas}R$, com uma comissão de 5%, sua comissão é de {comissao} R$ ")