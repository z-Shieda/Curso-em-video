import random

alunos = str(input("Digite o nome dos alunos de forma ESPACADA"))
alunos.split(alunos)
escolha = random.choice(alunos.split())

print("O aluno(a) escolhido é {}".format(escolha))



