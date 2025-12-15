from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    
    @abstractmethod
    def guardar_registro(self, entidad):
        raise NotImplementedError

    @abstractmethod
    def obtener_todos_los_registros(self) -> list:
        raise NotImplementedError  
    
    @abstractmethod
    def obtener_registro_por_filtro(self, filtros: dict):
        raise NotImplementedError   
