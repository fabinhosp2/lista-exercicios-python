import unittest

from aula005Exe021.ingresso import Normal

class MyTest(unittest.TestCase):
    def testFun(self):
        normal = Normal()

        self.assertEqual(normal.imprimeValor(),"Ingresso Normal")
        self.assertNotEqual(normal.imprimeValor(),"Ingresso Normal.")

if __name__ == '__main__':
    unittest.main()