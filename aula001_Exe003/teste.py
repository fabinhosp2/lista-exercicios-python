import unittest

from aula001_Exe003.calcula import Calculadora

class MyTest(unittest.TestCase):
    def testFun(self):
        calculadora = Calculadora()

        self.assertEqual(calculadora.soma(1,1),2)
        self.assertNotEqual(calculadora.soma(1,1),3)

if __name__ == '__main__':
    unittest.main()