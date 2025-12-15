from modules.repositorio_concreto import RepositorioReclamosSQLAlchemy, RepositorioUsuariosSQLAlchemy
from modules.config import crear_engine

def crear_repositorio():
#fabrica de repositorios
    session = crear_engine()
    repo_reclamo =  RepositorioReclamosSQLAlchemy(session())
    repo_usuario = RepositorioUsuariosSQLAlchemy(session())
    return repo_reclamo, repo_usuario

def obtener_personal(archivo_personal):
    usuarios = []
    with open(archivo_personal, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            usuario = {
                'nombre': datos[0],
                'apellido': datos[1],
                'email': datos[2],
                'username': datos[3],
                'claustro': datos[4],
                'password': datos[5],
                'rol': datos[6],
                'departamento': datos[7],
            }
            usuarios.append(usuario)
    return usuarios

def obtener_reclamos_similares(reclamo, lista_reclamos):
#calcula similitud textual entre reclamos
    palabras_en_reclamo = set(reclamo.lower().strip().replace(".", "").replace(",", "").split())
    
    if not palabras_en_reclamo:
        return []

    frases_similares_en_reclamo = []
    
    for r in lista_reclamos:
        palabras_existente = set(r['contenido'].lower().strip().replace(".", "").replace(",", "").split())
        if not palabras_existente:
            continue

        interseccion = palabras_en_reclamo.intersection(palabras_existente)
        union = palabras_en_reclamo.union(palabras_existente)
        similitud = len(interseccion) / len(union)

        if similitud >= 0.4:  # más permisivo que tu 50% original
            frases_similares_en_reclamo.append(r)

    return frases_similares_en_reclamo

