class SomaDasIdades:

    def verifica(self, idadeH1, idadeH2, idadeM1, idadeM2):



        if (idadeH1 > idadeH2):
            print("Homem com mais idade:", idadeH1)
            print("Homem com menos idade:", idadeH2)

            idademaiorH = idadeH1
            idademenorH = idadeH2
        else:
            print("Homem com mais idade:", idadeH2)
            print("Homem com menos idade:", idadeH1)

            idademaiorH = idadeH2
            idademenorH = idadeH1


        if (idadeM1 > idadeM2):
            print("Mulher com mais idade:", idadeM1)
            print("Mulher com menos idade:", idadeM2)

            idademaiorM = idadeM1
            idademenorM = idadeM2
        else:
            print("Mulher com mais idade:", idadeM2)
            print("Mulher com menos idade:", idadeM1)

            idademaiorM = idadeM2
            idademenorM = idadeM1


        print("Soma das idades do Homem e da Mulher de MAIOR idade", idademaiorH + idademaiorM)
        print("Soma das idades do Homem e da Mulher de MENOR idade", idademenorH + idademenorM)

