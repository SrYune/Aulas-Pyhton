import os
import time
import random

os.system("cls")

#Cadastro

contatos = []  # lista onde cada contato será guardado

continuar = "s"
while continuar.lower() == "s":
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    contato = {}
    contatos.append(contato)

    continuar = input("Deseja cadastrar outro contato? (s/n): ")

print("Contatos cadastrados:")
for c in contatos:
    print(f"{c['nome']} - {c['telefone']}")
    print(f"{c['nome']} - {c['telefone']}")
    # Pergunta se deseja continuar

    if continuar == "n":
        print("Sistema encerrado.")
        break  # Sai do loop
