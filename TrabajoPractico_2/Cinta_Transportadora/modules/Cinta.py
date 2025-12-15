from modules.Detector import DetectorAlimento
from modules.Alimento import Kiwi, Manzana, Papa, Zanahoria

class Cinta:
    def __init__ (self):
        self.__detector = DetectorAlimento ()
    
    def transportar_alimento (self):

        alimento_detectado = self.__detector.detectar_alimento ()
        if alimento_detectado ["alimento"] == "kiwi":
            tipo_alimento = Kiwi (alimento_detectado ["peso"])
        elif alimento_detectado ["alimento"] == "manzana":
            tipo_alimento = Manzana (alimento_detectado ["peso"])
        elif alimento_detectado ["alimento"] == "papa":
            tipo_alimento = Papa (alimento_detectado ["peso"])
        elif alimento_detectado ["alimento"] == "zanahoria":
            tipo_alimento = Zanahoria (alimento_detectado ["peso"])
        elif alimento_detectado ["alimento"] == "undefined":
            tipo_alimento = "undefined"       
        
        return tipo_alimento
 

        