import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.Modelos import Base
from modules.dominio import Reclamo
from modules.repositorio_concreto import RepositorioReclamosSQLAlchemy

class TestRepositorioReclamosSQLAlchemy(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.repo = RepositorioReclamosSQLAlchemy(self.session)

    def test_guardar_y_obtener(self):
        reclamo = Reclamo("pendiente", "contenido", "depto", 1, "2024-01-01", None, None, 2)
        self.repo.guardar_registro(reclamo)
        reclamos = self.repo.obtener_todos_los_registros()
        self.assertEqual(len(reclamos), 1)
        self.assertEqual(reclamos[0].contenido, "contenido")

    def test_modificar_registro(self):
        reclamo = Reclamo("pendiente", "contenido", "depto", 1, "2024-01-01", None, None, 2)
        self.repo.guardar_registro(reclamo)
        reclamos = self.repo.obtener_todos_los_registros()
        reclamo_mod = reclamos[0]
        reclamo_mod.estado = "resuelto"
        self.repo.modificar_registro(reclamo_mod)
        reclamos = self.repo.obtener_todos_los_registros()
        self.assertEqual(reclamos[0].estado, "resuelto")

if __name__ == "__main__":
    unittest.main()