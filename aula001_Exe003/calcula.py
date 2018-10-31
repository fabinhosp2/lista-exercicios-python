class Calculadora:

    def soma(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def divi(self, num1, num2):
        return num1 / num2

    def calcula_todos(self, num1, num2):

        print(f'As operações de {num1} e {num2}:')
        print(f'de soma é: {str(self.soma(num1, num2))}')
        print(f'de subtração é: {str(self.sub(num1, num2))}')
        print(f'de multiplicação é: {str(self.multi(num1, num2))}')
        print(f'de divisão é: {str(self.divi(num1, num2))}')

        print('=-' * 30)

        print(f'As operações de {num1} e {num2} + 1:')
        print(f'de soma é: {str(self.soma(num1, num2) + 1)}')
        print(f'de subtração é: {str(self.sub(num1, num2) + 1)}')
        print(f'de multiplicação é: {str(self.multi(num1, num2) + 1)}')
        print(f'de divisão é: {str(self.divi(num1, num2) + 1)}')