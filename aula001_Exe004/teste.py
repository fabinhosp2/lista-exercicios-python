import unittest

from aula001_Exe004.troco import Troco

class MyTest(unittest.TestCase):
    def testFun(self):
        troco = Troco()

        self.assertEqual(troco.calcula_troco(100,50,25),62.50)
        self.assertNotEqual(troco.calcula_troco(100,50,25),30)

if __name__ == '__main__':
    unittest.main()