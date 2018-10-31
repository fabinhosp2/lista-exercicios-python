import unittest

from num import Numero


class MyTest(unittest.TestCase):
    def testFun(self):
        numero = Numero()

        self.assertEqual(numero.verifica_numero(1), "UM")
        self.assertNotEqual(numero.verifica_numero(1), "UMM")


if __name__ == '__main__':
    unittest.main()
