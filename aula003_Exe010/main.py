from aula003_Exe010.verificaaluno import VerificaAluno

aluno = input("Informe o nome do aluno -> ")
n1 = float(input("Informe a N1 -> "))
n2 = float(input("Informe a N2 -> "))
n3 = float(input("Informe a N3 -> "))

verificaaluno = VerificaAluno()
verificaaluno.verificacao(aluno, n1, n2, n3)