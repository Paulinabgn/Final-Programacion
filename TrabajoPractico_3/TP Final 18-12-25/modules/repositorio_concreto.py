from modules.dominio import Reclamo, Usuario
from modules.repositorio_abstracto import RepositorioAbstracto
from modules.Modelos import ModeloReclamo, ModeloUsuario

    
class RepositorioReclamosSQLAlchemy(RepositorioAbstracto):
#implementa la persistenca con SQLAlchemy de los reclamos y usuarios

    def __init__(self, session):
        self.__session = session
        tabla_libro = ModeloReclamo()
        tabla_libro.metadata.create_all(self.__session.bind)

    def guardar_registro(self, reclamo):
        if not isinstance(reclamo, Reclamo):
            raise ValueError("El parámetro no es una instancia de la clase Reclamo")
        modelo_reclamos = self.__map_entidad_a_modelo(reclamo)
        self.__session.add(modelo_reclamos)
        self.__session.commit()

    def obtener_todos_los_registros(self):
        modelo_reclamos = self.__session.query(ModeloReclamo).all()
        return [self.__map_modelo_a_entidad(reclamo) for reclamo in modelo_reclamos]   
    
    def obtener_registro_por_filtro(self, filtro, valor):
        modelo_reclamos = self.__session.query(ModeloReclamo).filter_by(**{filtro:valor}).first()
        return self.__map_modelo_a_entidad(modelo_reclamos) if modelo_reclamos else None
    
    def obtener_registros_segun_filtro(self, filtro, valor):
        modelo_reclamos = self.__session.query(ModeloReclamo).filter_by(**{filtro:valor}).all()
        return [self.__map_modelo_a_entidad(reclamo) for reclamo in modelo_reclamos]

    def modificar_registro(self, reclamo_modificado):
        if not isinstance(reclamo_modificado, Reclamo):
            raise ValueError("El parámetro no es una instancia de la clase Reclamo")
        register = self.__session.query(ModeloReclamo).filter_by(id=reclamo_modificado.id).first()
        register.estado = reclamo_modificado.estado
        register.contenido = reclamo_modificado.contenido
        register.departamento = reclamo_modificado.departamento
        register.id_usuario = reclamo_modificado.id_usuario
        register.fecha_hora = reclamo_modificado.fecha_hora
        register.ruta_imagen = reclamo_modificado.ruta_imagen
        register.tiempo_de_resolucion = reclamo_modificado.tiempo_de_resolucion
        self.__session.commit()

    # ------------------------------------------------------------------------------------
    def obtener_registros_seguidos_por_usuario(self, id_usuario):
        modelo_usuario = self.__session.query(ModeloUsuario).filter_by(id=id_usuario).first()
        return [self.__map_modelo_a_entidad(reclamo) for reclamo in modelo_usuario.reclamos_seguidos]
    # ------------------------------------------------------------------------------------
    
    def __map_entidad_a_modelo(self, entidad: Reclamo):
        return ModeloReclamo(
            contenido=entidad.contenido,
            departamento=entidad.departamento,
            fecha_hora=entidad.fecha_hora,
            id_usuario=entidad.id_usuario,
            estado=entidad.estado,
            ruta_imagen=entidad.ruta_imagen,
            tiempo_de_resolucion=entidad.tiempo_de_resolucion 
        )
    
    def __map_modelo_a_entidad(self, modelo: ModeloReclamo):
        return Reclamo(
            modelo.estado,
            modelo.contenido,
            modelo.departamento,
            modelo.id_usuario,
            modelo.fecha_hora,
            modelo.ruta_imagen,
            modelo.id,
            modelo.tiempo_de_resolucion
        )
    
class RepositorioUsuariosSQLAlchemy(RepositorioAbstracto):
    def __init__(self, session):
        self.__session = session
        tabla_usuario = ModeloUsuario()
        tabla_usuario.metadata.create_all(self.__session.bind)

    def guardar_registro(self, usuario):
        if not isinstance(usuario, Usuario):
            raise ValueError("El parámetro no es una instancia de la clase Usuario")
        modelo_usuario = self.__map_entidad_a_modelo(usuario)
        self.__session.add(modelo_usuario)
        self.__session.commit()

    def obtener_todos_los_registros(self):
        modelo_usuarios = self.__session.query(ModeloUsuario).all()
        return [self.__map_modelo_a_entidad(usuario) for usuario in modelo_usuarios]   

    def asociar_registro(self, id, id_asociado):
        register = self.__session.query(ModeloUsuario).filter_by(id=id).first()
        modelo_reclamo = self.__session.query(ModeloReclamo).filter_by(id=id_asociado).first()
        register.reclamos_seguidos.append(modelo_reclamo)
        self.__session.commit()

    def obtener_seguidores_de_registro_asociado(self, id_asociado):
        modelo_reclamo = self.__session.query(ModeloReclamo).filter_by(id=id_asociado).first()
        return [self.__map_modelo_a_entidad(usuario) for usuario in modelo_reclamo.usuarios_seguidores]
    # ------------------------------------------------------------------------------------
    
    def obtener_registro_por_filtro(self, filtros: dict):
        modelo = self.__session.query(ModeloUsuario).filter_by(**filtros).first()
        return self.__map_modelo_a_entidad(modelo) if modelo else None
    
    def __map_entidad_a_modelo(self, entidad: Usuario):
        return ModeloUsuario(
            nombre=entidad.nombre,
            apellido=entidad.apellido,
            email=entidad.email,
            username=entidad.username,
            claustro=entidad.claustro,
            password=entidad.password,
            rol=entidad.rol,
            departamento=entidad.departamento
        )
    
    def __map_modelo_a_entidad(self, modelo: ModeloUsuario):
        return Usuario(
            modelo.id,
            modelo.nombre,
            modelo.apellido,
            modelo.email,
            modelo.username,
            modelo.claustro,
            modelo.password,
            modelo.rol,
            modelo.departamento
        )