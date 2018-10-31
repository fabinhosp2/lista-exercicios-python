class Funcionario:

    nome = ""
    idade = 0
    salario = 0

class Programador(Funcionario):

    def aumenta_salario(self):

        self.salario = self.salario + 20
        print(self.salario)

class Analista(Funcionario):

    def aumenta_salario(self):

        self.salario = self.salario + 30
        print(self.salario)

class Main:

    def main(self):

        programador = Programador()
        programador.aumenta_salario()

        analista = Analista()
        analista.aumenta_salario()