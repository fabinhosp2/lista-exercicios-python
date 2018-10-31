from volume import Volume

comp = float(input("Informe o Comprimento -> "))
larg = float(input("Informe a Largura     -> "))
alt = float(input("Informe a Altura      -> "))

volume = Volume()
volume.converteVolume(comp, larg, alt)