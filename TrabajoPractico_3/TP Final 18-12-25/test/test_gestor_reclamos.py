import unittest
from modules.gestor_reclamos import GestorDeReclamos
from modules.dominio import Reclamo
from modules.repositorio_abstracto import RepositorioAbstracto

class RepositorioFalsoReclamo (RepositorioAbstracto):
    def __init__ (self):
        self.__reclamos = []
        self.__next_id = 1
    
    def guardar_registro (self, reclamo):
        reclamo.id = self.__next_id
        self.__next_id += 1
        self.__reclamos.append(reclamo)
    
    def obtener_todos_los_registros(self):
        return self.__reclamos
    
    def obtener_registro_por_filtro(self, filtro, valor):
        for reclamo in self.__reclamos:
            if getattr(reclamo, filtro) == valor:
                return reclamo
        return None
    
    def modificar_registro(self, reclamo_modificado):
        for i, reclamo in enumerate(self.__reclamos):
            if reclamo.id == reclamo_modificado.id:
                self.__reclamos[i] = reclamo_modificado
                return
        raise ValueError("El reclamo no existe en el repositorio")

class TestGestorDeReclamos(unittest.TestCase):
    
    def test_agregar_reclamo (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("en proceso", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        self.assertIsNotNone(repo.obtener_registro_por_filtro("contenido", "Luz apagada")) #no se si es mejor asi o con el estado

    def test_listar_reclamos_existentes (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("en proceso", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        self.assertEqual(gestor.listar_reclamos_existentes(), [{"estado": "en proceso", "contenido": "Luz apagada", "departamento": "Maestranza", "id_usuario": 1, "fecha_hora": "10-12-2025 16:37", "id": 1, "tiempo_de_resolucion": 1}])
    
    def test_filtrar_reclamos_por_depto (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("en proceso", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        gestor.agregar_nuevo_reclamo("pendiente", "Computadora Laboratorio 1 no enciende", "Soporte informático", 2, "10-12-2025 18:30", "/ruta/imagen2.jpg")
        dpto_resultado = gestor.filtrar_reclamos_por_depto ("Maestranza")
        self.assertEqual(len(dpto_resultado), 1)
        self.assertEqual(dpto_resultado[0]["departamento"], "Maestranza")
    
    def test_devolver_reclamo (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("en proceso", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        reclamo_devuelto = gestor.devolver_reclamo(1)
        self.assertEqual(reclamo_devuelto, {"estado": "en proceso", "contenido": "Luz apagada", "departamento": "Maestranza", "id_usuario": 1, "fecha_hora": "10-12-2025 16:37", "id": 1, "tiempo_de_resolucion": 1})

    def test_filtrar_reclamo_por_contenido (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("en proceso", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        reclamo_filtrado = gestor.filtrar_reclamo_por_contenido("Luz apagada")
        self.assertEqual(reclamo_filtrado, {"estado": "en proceso", "contenido": "Luz apagada", "departamento": "Maestranza", "id_usuario": 1, "fecha_hora": "10-12-2025 16:37", "id": 1, "tiempo_de_resolucion": 1})

    def test_derivar (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("en proceso", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        gestor.derivar (1,"Soporte informático")
        self.assertEqual (repo.obtener_registro_por_filtro("id",1).departamento, "Soporte informático")

    def test_cambiar_estado_reclamo (self):
        repo = RepositorioFalsoReclamo()
        gestor = GestorDeReclamos(repo)
        gestor.agregar_nuevo_reclamo("pendiente", "Luz apagada", "Maestranza", 1, "10-12-2025 16:37", "/ruta/imagen.jpg")
        gestor.cambiar_estado_reclamo(1, "en proceso", 5)
        self.assertEqual (repo.obtener_registro_por_filtro("id",1).estado, "en proceso")
    

if __name__ == "__main__":
    unittest.main()