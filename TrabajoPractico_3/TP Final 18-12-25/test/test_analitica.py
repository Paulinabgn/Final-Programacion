import unittest
from modules.Analitica import Analitica

class TestAnalitica(unittest.TestCase):
    def setUp(self):
        self.reclamos = [
            {"estado": "pendiente", "contenido": "A", "departamento": "maestranza", "tiempo_de_resolucion": 2},
            {"estado": "resuelto", "contenido": "B", "departamento": "maestranza", "tiempo_de_resolucion": 3},
            {"estado": "en proceso", "contenido": "C", "departamento": "maestranza", "tiempo_de_resolucion": 7}
        ]
        self.analitica = Analitica(self.reclamos, "maestranza")

    def test_calcular_numero_de_reclamos(self):
        self.assertEqual(self.analitica.calcular_numero_de_reclamos(), 3)

    def test_calcular_porcentajes_estados(self):
        porcentajes = self.analitica.calcular_porcentajes_estados()
        self.assertEqual(porcentajes["pendiente"], 33.333333333333336)
        self.assertEqual(porcentajes["resuelto"], 33.333333333333336)
        self.assertEqual(porcentajes["en proceso"], 33.333333333333336)

    def test_calcular_mediana_de_resolucion (self):
        mediana_en_proceso = self.analitica.calcular_mediana_por_estado('en proceso')
        mediana_resuelto = self.analitica.calcular_mediana_por_estado('resuelto')
        self.assertEqual(mediana_en_proceso, 7) 
        self.assertEqual(mediana_resuelto, 3)

if __name__ == "__main__":
    unittest.main()