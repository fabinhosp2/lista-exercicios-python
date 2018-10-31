class Troco:

    def calcula_troco(self, vlpago, vlprod, desc):


        troco = vlpago - (vlprod * desc/100)
        print(f'troco é {troco}')
        return troco
