class Pessoa():

    def aluno(self, nome):
        print(f'O aluno {nome}', end='')

    def calcula_media(self, nota01, nota02, nota03):
        media = (nota01 + nota02 + nota03) /3
        print(f' e sua média foi {media}')

    def calcula_idade(self, idade):
            if idade >= 18:
                print("Sim, é maior de idade.")
                print('=-' * 30)

            else:
                print("Não é maior de idade.")
                print('=-' * 30)



