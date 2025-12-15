from modules.Cinta import Cinta
from modules.Cajon import Cajon
from modules.Calculadora import Calculadora
from modules.Alimento import Alimento, Fruta, Verdura, Kiwi, Manzana, Papa, Zanahoria

class Controlador:
    def __init__ (self, cant_alimentos):
        self.__cantidad_de_alimentos = cant_alimentos

    def llenar_cajon (self, cajon):
        cinta = Cinta ()
        contador = 0
        while (contador < self.__cantidad_de_alimentos):
            tipo_alimento = cinta.transportar_alimento ()
            if tipo_alimento != "undefined":
                cajon.agregar_alimento (tipo_alimento)
                contador += 1
        

    def calcular_resultados (self, cajon_lleno):
        calculadora = Calculadora ()
        resultados_dicc = {}
        peso_total_cajon = calculadora.calcular_peso_total_cajon (cajon_lleno)
        aw_kiwi = calculadora.calcular_prom_aw (cajon_lleno, Kiwi)
        aw_manzana = calculadora.calcular_prom_aw (cajon_lleno, Manzana)
        aw_papa = calculadora.calcular_prom_aw (cajon_lleno, Papa)
        aw_zanahoria = calculadora.calcular_prom_aw (cajon_lleno, Zanahoria)
        aw_fruta = calculadora.calcular_prom_aw (cajon_lleno, Fruta)
        aw_verdura = calculadora.calcular_prom_aw (cajon_lleno, Verdura)
        aw_total = calculadora.calcular_prom_aw (cajon_lleno, Alimento)
        resultados_dicc = {'peso_total' : peso_total_cajon, 'aw_kiwi': aw_kiwi, 'aw_manzana' : aw_manzana, 'aw_papa' : aw_papa, 'aw_zanahoria' : aw_zanahoria, 'aw_fruta' : aw_fruta, 'aw_verdura' : aw_verdura, 'aw_total' : aw_total}
        return resultados_dicc

    def alertar (self, resultados_dicc):
        if (resultados_dicc ["aw_kiwi"] > 0.90 or resultados_dicc ["aw_manzana"] > 0.90 or resultados_dicc ["aw_papa"] > 0.90 or resultados_dicc ["aw_zanahoria"] > 0.90 or resultados_dicc ["aw_fruta"] > 0.90 or resultados_dicc ["aw_verdura"] > 0.90 or resultados_dicc ["aw_total"] > 0.90):
            mensaje_de_advertencia = "ADVERTENCIA! Al menos uno de los promedios supera 0.90"
        else: 
            mensaje_de_advertencia = None
        return mensaje_de_advertencia
    
    