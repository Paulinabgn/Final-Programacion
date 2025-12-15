# import unittest
# from modules.gestor_usuarios import GestorDeUsuario
# from modules.dominio import Usuario
# from modules.repositorio_abstracto import RepositorioAbstracto

# class RepositorioFalsoUsuario (RepositorioAbstracto):
    
#     def __init__ (self):
#         self.__usuarios = []
#         self.__next_id = 1
    
#     def guardar_registro (self, usuario):
#         usuario.id = self.__next_id
#         self.__next_id += 1
#         self.__usuarios.append(usuario)
    
#     def obtener_todos_los_registros(self):
#         return self.__usuarios
    
#     def obtener_registro_por_filtro(self, filtro, valor):
#         for usuario in self.__usuarios:
#             if getattr(usuario, filtro) == valor:
#                 return usuario
#         return None
    
#     def modificar_registro(self, usuario_modificado):
#         for i, usuario in enumerate(self.__usuarios):
#             if usuario.id == usuario_modificado.id:
#                 self.__usuarios[i] = usuario_modificado
#                 return
#         raise ValueError("El usuario no existe en el repositorio")

# class TestGestotUsuario (unittest.TestCase):
#     def test_registrar_nuevo_usuario_existente (self):
#         repo = RepositorioFalsoUsuario()
#         gestor = GestorDeUsuario (repo)
#         usuario_nuevo = gestor.registrar_nuevo_usuario("Ana", "Gomez","anagomez@gmail.com", "anagomez", "Estudiante", "ana", "usuario_final")
#         self.assertIsNone (repo.obtener_registro_por_filtro({"email", usuario_nuevo.email})) #para verificar que no existe
#         self.assertIsNotNone (repo.obtener_registro_por_filtro ({"email", "paulinabugnon@gmail.com"})) #para verificar que ya existe

#         #gestor.registrar_nuevo_usuario("Ana", "Gómez", "ana@mail.com", "anagomez", "Estudiante", "ana", "usuario_final", "Soporte Informatico")
        
        
#         #self.assertIsNone(resultado)  # la función no devuelve nada al registrar OK
#         #self.assertEqual(len(repo.obtener_todos_los_registros()), 1)

#         #usuario_guardado = repo.obtener_todos_los_registros()[0]
#         #self.assertEqual(usuario_guardado.email, "ana@mail.com")
#         #self.assertEqual(usuario_guardado.nombre, "Ana")


# if __name__ == "__main__":
#     unittest.main()