from modules.dominio import Reclamo
from modules.repositorio_abstracto import RepositorioAbstracto


class GestorDeReclamos:
#usa el repo para persistencia, logica de alto nivel sobre reclamos

    def __init__(self, repo: RepositorioAbstracto): 
        self.__repo = repo
        self.__numero_reclamos = len(self.__repo.obtener_todos_los_registros())

    @property
    def numero_reclamos(self):
        return self.__numero_reclamos

    def listar_reclamos_existentes(self):
        registros = self.__repo.obtener_todos_los_registros()
        if not registros:
            return []
        return [reclamo.to_dict() for reclamo in registros]
    
    def filtrar_reclamos_por_depto(self, departamento):
        reclamo_por_depto = []
        registros = self.__repo.obtener_todos_los_registros()
        if not registros:
            return []
        else:
            reclamos = [reclamo.to_dict() for reclamo in registros]
            
        for i in reclamos:
            if i['departamento'].lower().strip() == departamento.lower().strip():
                reclamo_por_depto.append(i)
        return reclamo_por_depto

    def agregar_nuevo_reclamo(self, estado, contenido, departamento, id_usuario, fecha_hora, ruta_imagen,tiempo_de_resolucion=1):
        reclamo = Reclamo(estado,contenido,departamento,id_usuario,fecha_hora,ruta_imagen,None,tiempo_de_resolucion)
        self.__repo.guardar_registro(reclamo)
        self.__numero_reclamos += 1

    def devolver_reclamo(self, id_reclamo):
        return self.__repo.obtener_registro_por_filtro("id", id_reclamo).to_dict()
    
    def filtrar_reclamo_por_contenido(self, contenido):
        registro = self.__repo.obtener_registro_por_filtro("contenido", contenido)
        if registro is None:
            raise ValueError(f"No se encontro un reclamo con el contenido: {contenido}")
        return registro.to_dict()

    def derivar(self, id_reclamo, nuevo_depto):
        reclamo = self.__repo.obtener_registro_por_filtro("id", id_reclamo)
        if reclamo is None:
            raise ValueError("El reclamo no existe en la base de datos")
        id_usuario = int(reclamo.id_usuario)
        id_reclamo = int(id_reclamo)
        reclamo = Reclamo(reclamo.estado,reclamo.contenido,nuevo_depto,id_usuario,reclamo.fecha_hora,reclamo.ruta_imagen,id_reclamo, reclamo.tiempo_de_resolucion)
        self.__repo.modificar_registro(reclamo)

    def cambiar_estado_reclamo(self, id_reclamo, nuevo_estado, nuevo_tiempo_de_resolucion):
        reclamo = self.__repo.obtener_registro_por_filtro("id", id_reclamo)
        if reclamo is None:
            raise ValueError("El reclamo no existe en la base de datos")
        
        id_usuario = int(reclamo.id_usuario)
        reclamo = Reclamo(nuevo_estado,reclamo.contenido,reclamo.departamento,id_usuario,reclamo.fecha_hora,reclamo.ruta_imagen,reclamo.id, nuevo_tiempo_de_resolucion)
        self.__repo.modificar_registro(reclamo)
    
    def filtrar_reclamos_seguidos_por_usuario(self, id_usuario):
        return [reclamo.to_dict() for reclamo in self.__repo.obtener_registros_seguidos_por_usuario(id_usuario)]
    