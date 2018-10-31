class VerificaAluno:

    def verificacao(self, aluno, n1, n2, n3):

        mtotal = (n1 + n2 + n3) / 3


        if(mtotal >= 7):
            print(aluno, "está: Aprovado", "\nMédia -> ",round(mtotal, 1))

        else:
            print(aluno, "está: Reprovado", "\nMédia -> ",round(mtotal, 1))