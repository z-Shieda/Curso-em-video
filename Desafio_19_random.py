import random

aluno1 = input("Digite o nome do primeiro aluno")
aluno2 = input("Agora do Segundo")
aluno3 = input("Terceiro")
aluno4 = input("Quarto")

lista = [aluno1, aluno2, aluno3, aluno4]
escolha = random.choice (lista)
print("O aluno(a) escolhido é {}".format(escolha))