import os

os.system("cls")

#Entrada
nome = input("Insira seu nome:")
ano_nascimento = int(input("Insira seu ano de nascimento:"))
ano_atual = int(input("Insira o ano atual:"))

#Processamento
idade = ano_atual - ano_nascimento

#Saída
print(f"Olá {nome}, acredito que sua idade seja de {idade} anos.")