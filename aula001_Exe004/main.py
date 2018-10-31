from troco import Troco

vlprod = int (input("Informe o valor do produto"))

vlpago = int (input("Informe o valor pago"))

desc = int(input('Informe o desconto em "%": '))

troco = Troco()
troco.calcula_troco(vlpago, vlprod, desc)