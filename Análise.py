import os
os.system("cls")
 
nome = input("Digite seu nome:")
salario_atual = float(input("Digite seu salario atual:"))
 
 
if salario_atual <= 2.000:
    aumento_salario = salario_atual *0.10
    novo_salario = salario_atual + aumento_salario
    print("O seu novo salario é de:R$", novo_salario)
 
elif salario_atual <=5000:
    aumento_salario = salario_atual *0.7
    novo_salario = salario_atual + aumento_salario
    print("O seu novo salario é de:R$", novo_salario)
 
else:
    aumento_salario = salario_atual *0.5
    novo_salario = salario_atual + aumento_salario
    print("O seu novo salario é de:R$", novo_salario)
