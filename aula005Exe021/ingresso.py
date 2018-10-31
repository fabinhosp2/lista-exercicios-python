class Ingresso:

    valor = 100
    def imprimeValor(self):
        print(self.valor)

class Vip(Ingresso):

    def imprimeValor(self):
        self.valor = self.valor + 50
        print(self.valor)

class Normal(Ingresso):

    def imprimeValor(self):
            return "Ingresso Normal"

class CamaroteInferior:

    localizacao = "localização inferior"

    def acessoLocalizacao(Vip):
        return self.localizacao

    def imprimeLocalizacao(self):
        print(self.localizacao)

class CamaroteSuperior(Vip):

    def imprimeValor(self):
        self.valor = self.valor + 100
        print(self.valor)

    def retornaValor(self):
        return self.valor

class Main:

    def main(self):

        ingresso = Ingresso()
        ingresso.imprimeValor()

        vip = Vip()
        vip.imprimeValor()

        normal = Normal()
        normal.imprimeValor()

        camaroteinferior = CamaroteInferior()
        camaroteinferior.imprimeLocalizacao()