class Imovel:

    endereco = "Este é o endereço do Imóvel"
    preco = 100

class Novo(Imovel):

    def adiciona(self):
        self.preco = self.preco + 50

    def obterpreco(self):
        return self.preco

    def imprime(self):
        print(self.preco)

class Velho(Imovel):

    def diminui(self):
        self.preco = self.preco - 50

    def acessa(self):
        velho = Velho()
        velho.preco()

    def imprime(self):
        print(self.preco)


class Main:

    def main(self):

        novo = Novo()
        novo.imprime()
        novo.adiciona()
        novo.imprime()

        velho = Velho()
        velho.imprime()
        velho.diminui()
        velho.imprime()
