from somadasidades import SomaDasIdades

idadeH1 = int(input("Informa a idade do Homem 1 -> "))
idadeH2 = int(input("Informa a idade do Homem 2 -> "))

idadeM1 = int(input("Informa a idade da Mulher 1 -> "))
idadeM2 = int(input("Informa a idade da Mulher 2 -> "))

somadasidades = SomaDasIdades()
somadasidades.verifica(idadeH1, idadeH2, idadeM1, idadeM2)