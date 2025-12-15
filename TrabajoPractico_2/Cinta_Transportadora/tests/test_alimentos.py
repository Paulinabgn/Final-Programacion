import unittest
from modules.Alimento import Kiwi, Manzana, Papa, Zanahoria, Fruta, Verdura
import math

class TestAlimentos (unittest.TestCase):
    def test_Kiwi (self):
        kiwi = Kiwi (0.12)
        self.assertAlmostEqual (kiwi.calcular_aw (), 0.96 * ((1 - math.exp (-18 * 0.12)) / (1 + math.exp (-18 * 0.12))), places=2)

    def test_Manzana (self):
        manzana = Manzana (0.3)
        self.assertAlmostEqual (manzana.calcular_aw (), 0.97 * (((15 * 0.3)**2) / (1 + ((15 * 0.3)**2))), places=2)

    def test_Papa (self):
        papa = Papa (0.15)
        self.assertAlmostEqual (papa.calcular_aw (), 0.66 * (math.atan(18 * 0.15)), places=2)
    
    def test_Zanahoria (self):
        zanahoria = Zanahoria (0.5)
        self.assertAlmostEqual (zanahoria.calcular_aw (), 0.96 * (1 - math.exp(-10 * 0.5)), places=2)

if __name__ == '__main__':
    unittest.main()
