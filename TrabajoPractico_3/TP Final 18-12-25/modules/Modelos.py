from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
#Clase Modelo: define tablas ORM con SQLAlchemy

asociacion_usuarios_reclamos = Table('usuarios_reclamos', Base.metadata,
    Column('user_id', Integer, ForeignKey('usuarios.id')),
    Column('claims_id', Integer, ForeignKey('reclamos.id'))
)

class ModeloReclamo(Base):
    __tablename__ = 'reclamos'
    id = Column(Integer(), primary_key=True, unique=True)
    contenido = Column(String(1000), nullable=False)
    departamento = Column(String(1000), nullable=False)
    fecha_hora = Column(String(1000), nullable=False)
    id_usuario = Column(Integer(), nullable=False)
    estado = Column(String(1000), nullable=False)
    ruta_imagen = Column(String(1000), nullable=True)
    tiempo_de_resolucion = Column(Integer(), nullable=False, default=1) 

class ModeloUsuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True, unique=True)
    nombre = Column(String(1000), nullable=False)
    apellido = Column(String(1000), nullable=False)
    email = Column(String(1000), nullable=False, unique=True)
    username = Column(String(1000), nullable=False, unique=True)
    claustro = Column(String(1000), nullable=False)
    password = Column(String(1000), nullable=False)
    rol = Column(String(1000), nullable=False)
    departamento = Column(String(1000))
    
    reclamos_seguidos = relationship('ModeloReclamo', secondary=asociacion_usuarios_reclamos, backref= 'usuarios_seguidores')