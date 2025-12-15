class Reclamo:
    def __init__(self, p_estado, p_contenido, p_departamento, p_id_usuario, p_fecha_hora, p_ruta_imagen, p_id,p_tiempo_de_resolucion=1):
        self.estado = p_estado
        self.contenido = p_contenido
        self.departamento = p_departamento
        self.id_usuario = p_id_usuario
        self.fecha_hora = p_fecha_hora
        self.ruta_imagen = p_ruta_imagen
        self.id = p_id
        self.tiempo_de_resolucion = p_tiempo_de_resolucion

    @property
    def estado(self):
        return self.__estado
    
    @property
    def contenido(self):
        return self.__contenido
    
    @property
    def departamento(self):
        return self.__departamento
    
    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @property
    def id(self):
        return self.__id
    
    @property
    def tiempo_de_resolucion(self):
        return self.__tiempo_de_resolucion
    
    @estado.setter
    def estado(self, p_estado):
        if isinstance(p_estado, str) and p_estado != "":
            self.__estado = p_estado
        else:
            raise TypeError("El estado debe ser un string y no estar vacio")

    @contenido.setter
    def contenido(self, p_contenido):
        if isinstance(p_contenido, str) and p_contenido != "":
            self.__contenido = p_contenido
        else:
            raise TypeError("El contenido debe ser un string y no estar vacio")
        
    @departamento.setter
    def departamento(self, p_departamento):
        if isinstance(p_departamento, str) and p_departamento != "":
            self.__departamento = p_departamento
        else:
            raise TypeError("El departamento debe ser un string y no estar vacio")
        
    @id_usuario.setter
    def id_usuario(self, p_id_usuario):
        if p_id_usuario != None:
            if not isinstance(p_id_usuario, int):
                raise TypeError("El id del usuario debe ser un número entero")
            self.__id_usuario = p_id_usuario
        else:
            self.__id_usuario = None
            
    @fecha_hora.setter
    def fecha_hora(self, p_fecha_hora):
        if isinstance(p_fecha_hora, str) and p_fecha_hora != "":
            self.__fecha_hora = p_fecha_hora
        else:
            raise TypeError("La fecha y hora debe ser un string y no estar vacio")
        
    @id.setter
    def id(self, p_id):
        if p_id != None:
            if not isinstance(p_id, int):
                raise TypeError("El id del reclamo debe ser un número entero")
            self.__id = p_id
        else:
            self.__id = None
         
    @tiempo_de_resolucion.setter
    def tiempo_de_resolucion(self, p_tiempo_de_resolucion):
        if isinstance(p_tiempo_de_resolucion, int) and p_tiempo_de_resolucion >= 1 and p_tiempo_de_resolucion <= 15:
            self.__tiempo_de_resolucion = p_tiempo_de_resolucion
        else:
            raise TypeError ("El tiempo de resolución debe ser un número entero entre 1 y 15")
    
    def to_dict(self):
        return {
            "estado": self.estado,
            "contenido": self.contenido,
            "departamento": self.departamento,
            "id_usuario": self.id_usuario,
            "fecha_hora": self.fecha_hora,
            "id": self.id,
            "tiempo_de_resolucion": self.tiempo_de_resolucion,
        }


class Usuario:
    def __init__(self, p_id, p_nombre, p_apellido, p_email, p_username, p_claustro, p_password, p_rol, p_departamento=None):
        self.id = p_id
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.email = p_email
        self.username = p_username
        self.claustro = p_claustro
        self.password = p_password
        self.rol = p_rol
        self.departamento = p_departamento

    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def username(self):
        return self.__username

    @property
    def claustro(self):
        return self.__claustro
    
    @property
    def password(self):
        return self.__password
    
    @property
    def rol(self):
        return self.__rol

    @property
    def departamento(self):
        return self.__departamento
    
    @id.setter
    def id(self, p_id):
        if p_id != None:
            if not isinstance(p_id, int):
                raise TypeError("El id debe ser un número entero")
            self.__id = p_id
        else:
            self.__id = None

    @nombre.setter
    def nombre(self, p_nombre):
        if isinstance(p_nombre, str) and p_nombre != "": 
            self.__nombre = p_nombre
        else:
            raise TypeError("El nombre debe ser un string y no estar vacio")
    
    @apellido.setter
    def apellido(self, p_apellido):
        if isinstance(p_apellido, str) and p_apellido != "": 
            self.__apellido = p_apellido
        else:
            raise TypeError("El apellido debe ser un string y no estar vacio")
        
    @email.setter
    def email(self, p_email):
        if isinstance(p_email, str) and p_email != "": 
            self.__email = p_email
        else:
            raise TypeError("El email debe ser un string y no estar vacio")

    @username.setter
    def username(self, p_username):
        if isinstance(p_username, str) and p_username != "": 
            self.__username = p_username
        else:
            raise TypeError("El nombre de usuari debe ser un string y no estar vacio")

    @claustro.setter
    def claustro(self, p_claustro):
        if isinstance(p_claustro, str) and p_claustro != "": 
            self.__claustro = p_claustro
        else:
            raise TypeError("El claustro debe ser un string y no estar vacio")
        
    @password.setter
    def password(self, p_password):
        if isinstance(p_password, str) and p_password != "": 
            self.__password = p_password
        else:
            raise TypeError("La contreseña debe ser un string y no estar vacio")

    @rol.setter
    def rol(self, p_rol):
        if isinstance(p_rol, str) and p_rol != "": 
            self.__rol = p_rol
        else:
            raise TypeError("El rol debe ser un string y no estar vacio")
            
    @departamento.setter
    def departamento(self, p_departamento):
        if p_departamento != None:
            if not isinstance(p_departamento, str):
                raise TypeError("El departamento del usuario debe ser un string")
            self.__departamento = p_departamento
        else:
            self.__departamento = None


    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "username": self.username,
            "claustro": self.claustro,
            "password": self.password,
            "rol": self.rol,
            "departamento": self.departamento
        }
        