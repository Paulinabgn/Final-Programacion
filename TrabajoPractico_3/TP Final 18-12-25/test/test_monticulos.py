import unittest
from modules.Monticulos import MonticuloBinario, MonticuloMediana

class TestMonticuloMediana (unittest.TestCase):
    def test_agregar_dato_y_calcular_mediana (self):
        mont_med = MonticuloMediana()
        mont_med.agregar_dato(10)
        self.assertEqual(mont_med.calcular_mediana(), 10)
    
    def test_agregar_dos_datos_y_calcular_mediana (self):
        mont_med = MonticuloMediana()
        mont_med.agregar_dato(10)
        mont_med.agregar_dato(20)
        self.assertEqual(mont_med.calcular_mediana(), 15) #cuando son dos datos, la mediana, es el promedio de ellos (10+20)/2 = 15

    def test_agregar_datos_desordenados_y_calcular_mediana (self):
        mont_med = MonticuloMediana()
        datos = [5, 1, 9, 3, 8]
        mediana_esperada = [5, 3, 5, 4, 5] #Valores de mediana esperada al agregar cada dato
        for i in range(len(datos)):
            mont_med.agregar_dato(datos[i]) #agrega el dato
            mediana_calculada = mont_med.calcular_mediana() #calcula la mediana de los datos agregados
            self.assertEqual(mediana_calculada, mediana_esperada[i]) #la compara con la mediana esperada
    
    def test_agregar_numeros_negativos_y_calcular_mediana (self):
        mont_med = MonticuloMediana()
        datos = [-5, -10, -1]
        for i in range (len(datos)):
            mont_med.agregar_dato(datos[i])
        mediana_calculada = mont_med.calcular_mediana()
        self.assertEqual(mediana_calculada, -5)
    
    def test_agregar_numeros_repetidos_y_calcular_mediana (self):
        mont_med = MonticuloMediana()
        mont_med.agregar_dato(7)
        mont_med.agregar_dato(7)
        mont_med.agregar_dato(7)
        mediana_calculada = mont_med.calcular_mediana()
        self.assertEqual(mediana_calculada, 7)
    
    def test_agregar_cantidad_de_datos_impares_y_calcular_mediana (self): #si yo agrego una cantidad impar de datos, la mediana es el valor del medio
        mont_med =MonticuloMediana()
        datos = [2,5,10,15,20]
        for i in range (len(datos)):
            mont_med.agregar_dato(datos[i])
        mediana_calculada = mont_med.calcular_mediana()
        self.assertEqual(mediana_calculada, 10)
    
    def test_agregar_cantidad_de_datos_pares_y_calcular_mediana (self): #si yo agrego una cantidad par de datos, la mediana es el promedio de los dos valores del medio
        mont_med = MonticuloMediana()
        datos = [2,4,10,15]
        for i in range (len(datos)):
            mont_med.agregar_dato(datos[i])
        mediana_calculada = mont_med.calcular_mediana()
        self.assertEqual(mediana_calculada, 7)


class TestMonticuloBinario (unittest.TestCase):
    
    def test_inertar_y_obtener_maximo (self):
        mont_bin = MonticuloBinario(es_max=True)
        mont_bin.insertar(10)
        mont_bin.insertar(5)
        mont_bin.insertar(20)
        max = mont_bin.obtener_max()
        self.assertEqual(max, 20)
    
    def test_inertar_y_obtener_minimo (self):
        mont_bin = MonticuloBinario(es_max=False)
        mont_bin.insertar(10)
        mont_bin.insertar(5)
        mont_bin.insertar(20)
        min = mont_bin.obtener_min()
        self.assertEqual(min, 5)
    
    def test_insertar_datos_y_eliminar_el_maximo (self):
        mont_bin = MonticuloBinario(es_max=True)
        datos = [3, 4, 7, 10]
        for i in range(len(datos)):
            mont_bin.insertar(datos[i])
        eliminado = mont_bin.eliminar()
        self.assertEqual(eliminado, 10)

    def test_insertar_datos_y_eliminar_el_minimo (self):
            mont_bin = MonticuloBinario(es_max=False)
            datos = [3, 4, 7, 10]
            for i in range(len(datos)):
                mont_bin.insertar(datos[i])
            eliminado = mont_bin.eliminar()
            self.assertEqual(eliminado, 3)


if __name__ == "__main__":
    unittest.main()