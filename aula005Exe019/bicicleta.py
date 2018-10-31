class Bicicleta:

    def quantidadeMarchas(self):
        print("24 Marchas")

    def tipoFreio(self):
        print("Freio V Break")

    def marca(self):
        print("Barra Forte")

class BicicletaPasseio(Bicicleta):

    def quantidadeMarchas(self):
        print("18 Marchas")

class BicicletaProfissional(Bicicleta):

    def quantidadeMarchas(self):
        print("30 Marchas")

class Main:

    def main(self):

        bicicleta = Bicicleta()
        bicicleta.quantidadeMarchas()

        bicicletapasseio = BicicletaPasseio()
        bicicletapasseio.quantidadeMarchas()

        bicicletaprofissional = BicicletaProfissional()
        bicicletaprofissional.quantidadeMarchas()