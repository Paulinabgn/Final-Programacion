from abc import ABC, abstractmethod
from modules.dominio import Reclamo

class Clasificador(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def clasificar(reclamo: Reclamo):
        pass