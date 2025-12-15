from modules.Alimento import Alimento ,Fruta, Verdura, Kiwi, Manzana, Papa, Zanahoria
from modules.Cajon import Cajon

class Calculadora:
    def __init__ (self):
        pass

    def calcular_peso_total_cajon (self, cajon):
        peso_total = 0
        for alimento in cajon:
            if isinstance (alimento, Alimento):
                peso_total += alimento.masa
            else:
                pass
        return round (peso_total, 2)

    def calcular_prom_aw (self, cajon, tipo_alimento):
        acum_tipo_alimento = 0
        cont = 0
        for alimento in cajon:
            if isinstance (alimento, tipo_alimento):
                acum_tipo_alimento += alimento.calcular_aw()
                cont += 1
        if cont == 0:
            return 0
        
        return round (acum_tipo_alimento / cont , 2)

        
        """lista_prom_kiwi = []
        lista_prom_manzana = []
        lista_prom_papa = []
        lista_prom_zanahoria = []
        lista_prom_fruta = []
        lista_prom_verdura = []
        lista_prom_total = []

        for alimento in cajon_alimentos:
            aw_alimento = alimento.calcular_aw ()
            aw_alimento = round (aw_alimento, 2)
            lista_prom_total.append (aw_alimento)

            if isinstance (alimento, Kiwi):
                kiwi = alimento.calcular_aw ()
                kiwi = round (kiwi, 2)
                lista_prom_kiwi.append (kiwi)
                lista_prom_fruta.append (kiwi)
            elif isinstance (alimento, Manzana):
                manzana = alimento.calcular_aw ()
                manzana = round (manzana, 2)
                lista_prom_manzana.append (manzana)
                lista_prom_fruta.append (manzana)
            elif isinstance (alimento, Papa):
                papa = alimento.calcular_aw ()
                papa = round (papa, 2)
                lista_prom_papa.append(papa)
                lista_prom_verdura.append (papa)
            elif isinstance (alimento, Zanahoria):
                zanahoria = alimento.calcular_aw ()
                zanahoria = round (zanahoria, 2)
                lista_prom_zanahoria.append (zanahoria)
                lista_prom_verdura.append (zanahoria)

                
        aw_kiwi = sum (lista_prom_kiwi) / len(lista_prom_kiwi) if lista_prom_kiwi else 0
        aw_manzana = sum (lista_prom_manzana) / len (lista_prom_manzana) if lista_prom_manzana else 0
        aw_papa = sum (lista_prom_papa) / len (lista_prom_papa) if lista_prom_papa else 0
        aw_zanahoria = sum (lista_prom_zanahoria) / len (lista_prom_zanahoria) if lista_prom_zanahoria else 0
        aw_fruta = sum(lista_prom_fruta) / len (lista_prom_fruta) if lista_prom_fruta else 0
        aw_verdura = sum (lista_prom_verdura) / len (lista_prom_verdura) if lista_prom_verdura else 0
        aw_total = sum (lista_prom_total) / len (lista_prom_total) if lista_prom_total else 0

        return round (aw_kiwi, 2), round (aw_manzana, 2), round (aw_papa, 2), round (aw_zanahoria, 2), round (aw_fruta, 2), round (aw_verdura, 2), round (aw_total, 2)"""
    