#from NOMEDOARQUIVO import NOMEDACLASSE
from pessoa import Pessoa

for i in range(5):
    nome = (input('Digite o nome do aluno: '))
    #Convertendo para inteiro
    idade = (int(input("Informe sua idade: ")))
    nota01 = (float(input('Informe sua primeira nota: ')))
    nota02 = (float(input('Informe sua segunda nota: ')))
    nota03 = (float(input('Informe sua terceira nota: ')))

    #Criando objeto
    pessoa = Pessoa()

    pessoa.aluno(nome)
    pessoa.calcula_media(nota01, nota02, nota03)
    pessoa.calcula_idade(idade)

