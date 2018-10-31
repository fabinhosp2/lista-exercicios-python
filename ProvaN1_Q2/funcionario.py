class Funcionario:

    nome = ""
    idade = 0
    salario = 500

    def aumenta_salario(self):

        self.salario = self.salario + 10
        print('Salário do Funcionário', self.salario)

class Programador(Funcionario):

    def aumenta_salario(self):

        self.salario = self.salario + 20
        print('Salário do Programador', self.salario)
        return self.salario

class Analista(Funcionario):

    def aumenta_salario(self):

        self.salario = self.salario + 30
        print('Salário do Analista', self.salario)

class Main:

    def main(self):

        funcionario = Funcionario()
        funcionario.aumenta_salario()

        programador = Programador()
        programador.aumenta_salario()

        analista = Analista()
        analista.aumenta_salario()

