class Animal:

    def comer(self):
        print("O animal está comento")

class Cachorro(Animal):

    def comer(self):
        print("O cachorro está comento sentado")

class Cavalo(Animal):

    def comer(self):
        print("O cavalo está comento em pé")

class Gato(Animal):

    def comer(self):
        print("O gato está comendo deitado")

class AnimalTeste:

    def listaAnimais(self):

        cachorro = Cachorro()
        cavalo = Cavalo()
        gato = Gato()

        listaDeAnimais = [cachorro, cavalo, gato]

        for i in listaDeAnimais:
            i.comer()
