import unittest
from modules.Calculadora import Calculadora
from modules.Alimento import Kiwi, Manzana, Papa, Zanahoria

class TestCalculadora (unittest.TestCase):
    def setUp (self):
        self.calculadora = Calculadora ()
        self.cajon = [Kiwi (0.2), Kiwi (0.5), Manzana (0.2), Manzana (0.5), Papa (0.2), Papa (0.5), Zanahoria (0.2), Zanahoria (0.5)]


    def test_calcular_peso_total_cajon (self):
        peso_total = self.calculadora.calcular_peso_total_cajon (self.cajon)
        self.assertAlmostEqual (peso_total, 2.8, places = 1)

    def tet_calcular_prom_aw (self):
        aw_kiwi, aw_manzana, aw_papa, aw_zanahoria, aw_fruta, aw_verdura, aw_total = self.calculadora.calcular_prom_aw (self.cajon)  
        self.assertAlmostEqual (aw_kiwi, 0.93, places = 2)
        self.assertAlmostEqual (aw_manzana, 0.92, places = 2)
        self.assertAlmostEqual (aw_papa, 0.07, places = 2)
        self.assertAlmostEqual (aw_zanahoria, 0.60, places = 2)
        self.assertAlmostEqual (aw_fruta, 0.92, places = 2)
        self.assertAlmostEqual (aw_verdura, 0.48, places = 2)
        self.assertAlmostEqual (aw_total, 0.70, places = 2)

if __name__ == "__main__":
    unittest.main ()