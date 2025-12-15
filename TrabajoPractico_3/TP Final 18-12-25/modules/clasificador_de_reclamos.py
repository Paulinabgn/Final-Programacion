#from modules.classifier import ClaimsClassifier
import pickle #modelo serializado
from modules.clasificador import Clasificador

class ClasificadorDeReclamos (Clasificador):
    def __init__(self):
        with open('./data/claims_clf.pkl', 'rb') as archivo:
            self.__clasificador = pickle.load(archivo)
    
    def clasificar(self, reclamos:list):
        return self.__clasificador.clasificar(reclamos)