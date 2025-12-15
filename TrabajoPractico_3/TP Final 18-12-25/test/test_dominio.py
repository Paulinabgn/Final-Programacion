import unittest
from modules.dominio import Reclamo, Usuario

class TestDominio(unittest.TestCase):

    def setUp(self):
        self.reclamo = Reclamo(
            p_estado="Pendiente",
            p_contenido="Falta de suministro",
            p_departamento="Servicios Públicos",
            p_id_usuario=1,
            p_fecha_hora="2024-11-22 10:00:00",
            p_ruta_imagen=None,
            p_id=123,
            p_tiempo_de_resolucion=5
        )
        self.usuario = Usuario(
            p_id=1,
            p_nombre="Juan",
            p_apellido="Pérez",
            p_email="juan@mail.com",
            p_username="juanp",
            p_claustro="alumno",
            p_password="1234",
            p_rol="usuario_final",
            p_departamento="Servicios Públicos"
        )

    # Tests para Reclamo
    def test_reclamo_init(self):
        self.assertEqual(self.reclamo.estado, "Pendiente")
        self.assertEqual(self.reclamo.contenido, "Falta de suministro")
        self.assertEqual(self.reclamo.departamento, "Servicios Públicos")
        self.assertEqual(self.reclamo.id_usuario, 1)
        self.assertEqual(self.reclamo.fecha_hora, "2024-11-22 10:00:00")
        self.assertEqual(self.reclamo.id, 123)
        self.assertEqual(self.reclamo.tiempo_de_resolucion, 5)

    def test_reclamo_setters_valid(self):
        self.reclamo.estado = "Resuelto"
        self.reclamo.contenido = "Nuevo contenido"
        self.reclamo.departamento = "Otro"
        self.reclamo.id_usuario = 2
        self.reclamo.fecha_hora = "2024-12-01 09:00:00"
        self.reclamo.id = 456
        self.reclamo.tiempo_de_resolucion = 10
        self.assertEqual(self.reclamo.estado, "Resuelto")
        self.assertEqual(self.reclamo.contenido, "Nuevo contenido")
        self.assertEqual(self.reclamo.departamento, "Otro")
        self.assertEqual(self.reclamo.id_usuario, 2)
        self.assertEqual(self.reclamo.fecha_hora, "2024-12-01 09:00:00")
        self.assertEqual(self.reclamo.id, 456)
        self.assertEqual(self.reclamo.tiempo_de_resolucion, 10)

    def test_reclamo_setters_invalid(self):
        with self.assertRaises(TypeError):
            self.reclamo.estado = ""
        with self.assertRaises(TypeError):
            self.reclamo.contenido = 123
        with self.assertRaises(TypeError):
            self.reclamo.departamento = ""
        with self.assertRaises(TypeError):
            self.reclamo.id_usuario = "abc"
        with self.assertRaises(TypeError):
            self.reclamo.fecha_hora = ""
        with self.assertRaises(TypeError):
            self.reclamo.id = "id"
        with self.assertRaises(TypeError):
            self.reclamo.tiempo_de_resolucion = 0

    def test_reclamo_to_dict(self):
        d = self.reclamo.to_dict()
        self.assertEqual(d["estado"], "Pendiente")
        self.assertEqual(d["contenido"], "Falta de suministro")
        self.assertEqual(d["departamento"], "Servicios Públicos")
        self.assertEqual(d["id_usuario"], 1)
        self.assertEqual(d["fecha_hora"], "2024-11-22 10:00:00")
        self.assertEqual(d["id"], 123)
        self.assertEqual(d["tiempo_de_resolucion"], 5)

    # Tests para Usuario
    def test_usuario_init(self):
        self.assertEqual(self.usuario.id, 1)
        self.assertEqual(self.usuario.nombre, "Juan")
        self.assertEqual(self.usuario.apellido, "Pérez")
        self.assertEqual(self.usuario.email, "juan@mail.com")
        self.assertEqual(self.usuario.username, "juanp")
        self.assertEqual(self.usuario.claustro, "alumno")
        self.assertEqual(self.usuario.password, "1234")
        self.assertEqual(self.usuario.rol, "usuario_final")
        self.assertEqual(self.usuario.departamento, "Servicios Públicos")

    def test_usuario_setters_valid(self):
        self.usuario.nombre = "Ana"
        self.usuario.apellido = "García"
        self.usuario.email = "ana@mail.com"
        self.usuario.username = "anag"
        self.usuario.claustro = "docente"
        self.usuario.password = "abcd"
        self.usuario.rol = "admin"
        self.usuario.departamento = "Otro"
        self.assertEqual(self.usuario.nombre, "Ana")
        self.assertEqual(self.usuario.apellido, "García")
        self.assertEqual(self.usuario.email, "ana@mail.com")
        self.assertEqual(self.usuario.username, "anag")
        self.assertEqual(self.usuario.claustro, "docente")
        self.assertEqual(self.usuario.password, "abcd")
        self.assertEqual(self.usuario.rol, "admin")
        self.assertEqual(self.usuario.departamento, "Otro")

    def test_usuario_setters_invalid(self):
        with self.assertRaises(TypeError):
            self.usuario.nombre = ""
        with self.assertRaises(TypeError):
            self.usuario.apellido = 123
        with self.assertRaises(TypeError):
            self.usuario.email = ""
        with self.assertRaises(TypeError):
            self.usuario.username = ""
        with self.assertRaises(TypeError):
            self.usuario.claustro = ""
        with self.assertRaises(TypeError):
            self.usuario.password = ""
        with self.assertRaises(TypeError):
            self.usuario.rol = ""
        with self.assertRaises(TypeError):
            self.usuario.departamento = 123

    def test_usuario_to_dict(self):
        d = self.usuario.to_dict()
        self.assertEqual(d["id"], 1)
        self.assertEqual(d["nombre"], "Juan")
        self.assertEqual(d["apellido"], "Pérez")
        self.assertEqual(d["email"], "juan@mail.com")
        self.assertEqual(d["username"], "juanp")
        self.assertEqual(d["claustro"], "alumno")
        self.assertEqual(d["password"], "1234")
        self.assertEqual(d["rol"], "usuario_final")
        self.assertEqual(d["departamento"], "Servicios Públicos")