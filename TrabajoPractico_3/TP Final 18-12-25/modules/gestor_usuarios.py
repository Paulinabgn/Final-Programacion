from modules.dominio import Usuario
from modules.repositorio_abstracto import RepositorioAbstracto

class GestorDeUsuario:
#controla la logica sobre usuarios y su vinculacion con reclamos

    def __init__(self, repo: RepositorioAbstracto):
        self.__repo = repo

    def registrar_nuevo_usuario(self, nombre, apellido, email, username, claustro, password, rol, departamento=None):
        if self.__repo.obtener_registro_por_filtro({"email": email}):
            return None
        #if self.__repo.obtener_registro_por_filtro("username", username):
        #    return None

        nuevo_usuario = Usuario(None,nombre,apellido,email,username,claustro,password,rol,departamento)
        self.__repo.guardar_registro(nuevo_usuario)

    def autenticar_usuario(self, filtros):
        usuario = self.__repo.obtener_registro_por_filtro(filtros)
        if not usuario:
            return None
        return usuario.to_dict()
    
    def cargar_usuario(self, id_usuario):
        registro = self.__repo.obtener_registro_por_filtro({"id": id_usuario})
        if registro is None:
            return None
        return registro.to_dict()
        #return self.__repo.obtener_registro_por_filtro("id",id_usuario).to_dict()
    
    def registrar_reclamo_a_seguir(self, id_usuario, id_reclamo):
        usuario = self.__repo.obtener_registro_por_filtro({"id": id_usuario})
        if not usuario:
            raise ValueError("El usuario no está registrado.")
        self.__repo.asociar_registro(id_usuario, id_reclamo)

    def obtener_cantidad_de_usuarios_adheridos(self,id_reclamo):
        return len(self.__repo.obtener_seguidores_de_registro_asociado(id_reclamo))
    
    def obtener_usuarios_adheridos_al_reclamo (self,id_reclamo):
        ids_usuarios_adheridos=[]
        usuarios_adheridos = self.__repo.obtener_seguidores_de_registro_asociado(id_reclamo)
        for i in usuarios_adheridos:
            ids_usuarios_adheridos.append(i.id)
        return ids_usuarios_adheridos

    def obtener_usuario(self,id_usuario):
        registro = self.__repo.obtener_registro_por_filtro({"id": id_usuario})
        if registro is None:
            return None
        return registro.to_dict()
        # return self.__repo.obtener_registro_por_filtro("id", id_usuario).to_dict()
    
        
        