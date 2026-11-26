import os

os.system("cls")

#Entrada
aluno = input("Insira nome do Aluno:")
notas_apostila = float(input("Insira a nota da Apostila:"))
notas_trabalho = float(input("Insira a nota do trabalho:"))
notas_prova = float(input("Insira a nota da prova:"))

#Processamento
média = (notas_apostila + notas_trabalho + notas_prova) / 3

#Saída
if média >= 7:
    print(f"O {aluno} passou, com a nota final de {média:.1f}")
elif média >= 4:
    print(f"O {aluno} infelizmente está de recuperação e grave risco de reprovar. Sua nota final foi {média:.1f}")
else:
    print(f"O {aluno} está reprovado devido a falta de notas que foram requisitadas.Sua nota final foi {média:.1f}")