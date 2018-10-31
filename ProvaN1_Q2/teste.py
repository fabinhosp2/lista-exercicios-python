import unittest

from ProvaN1_Q2.funcionario import Programador

class MyTest(unittest.TestCase):
    def testFun(self):
        programador = Programador()

        self.assertEqual(programador.aumenta_salario(20),520)
        self.assertNotEqual(programador.aumenta_salario(20),600)

if __name__ == '__main__':
    unittest.main()