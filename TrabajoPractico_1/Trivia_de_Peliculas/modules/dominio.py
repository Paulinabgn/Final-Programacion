"""La capa de dominio es la responsable de representar los conceptos específicos de la 
aplicación y sus reglas. Esta capa define cómo se deben manejar los datos y qué operaciones son validas
dentro del contexto específico de la aplicación.
La capa de dominio no debe depender de funciones y variables de flask como session, no debe depender 
de cual sea la interfaz de usuario ni de cómo se almacenan los datos.
"""
from modules.persistencia import generar_grafico_ejes,generar_grafico_torta, registrar_historial, obtener_frases_peliculas, obtener_historial
import random 

def crear_trivia (info, numero_frases= 1):
    """Se crea una trivia donde el usuario ingresara un numero especifico de frases que sera seleccionadas al azar.
    Argumentos:
    info(list): lista de tuplas donde en cada tupla esta almacenada una frase y su pelicula correspondiente.
    numero_frases (int, optional): el numero de frases a jugar. Por defecto es 1.
    
    Returns:
    list: una lista de diccionarios, donde cada uno representa la frase, las opciones de peliculas y la opcion correcta."""

    trivia = []
    frases_aleatorias = random.sample(info, numero_frases) #elije las frases aleatorias y unicas
    
    for frase, pelicula_correcta in frases_aleatorias:
        opciones = [pelicula_correcta]
        peliculas_disponibles = [pelicula for _, pelicula in info if pelicula != pelicula_correcta]
        opciones_incorrectas = random.sample(peliculas_disponibles, min(2, len(peliculas_disponibles))) #elije al azar dos peliculas distintas a la correcta
        opciones.extend(opciones_incorrectas)
        random.shuffle(opciones) #mezcla las opciones para que la correcta no este siempre primera
        trivia.append({"frase": frase, "opciones": opciones, "pelicula_correcta": pelicula_correcta})

    return trivia

def verificar_respuesta (respuesta_usuario, respuesta_correcta):
    """Verifica la respuesta del usuario en comparacion con la respuesta correcta.
    
    Argumentos:
    respuesta_usuario(str): respuesta seleccionada por el usuario.
    respuesta_correcta(str): respuesta correcta.
    
    Returns:
    str: mensaje que indica si la respuesta es correcta o incorrecta."""

    if respuesta_usuario == respuesta_correcta:
        return "¡Felicitaciones! La respuesta es correcta."
    else:
        return f"¡Incorrecto! La respuesta es: {respuesta_correcta}."

def ordenar_peliculas (lista):
    """Toma una lista de tuplas donde el segundo elemento de cada tupla es el titulo de la pelicula.
    Se devuelve una lista con las peliculas ordenadas alfabeticamente.
    
    Argumentos:
    lista: lista de tuplas.
    
    Returns: 
    Lista ordenada alfabeticamente con la primer letra de cada titulo en mayuscula."""

    peliculas = set() 
    cambios = []

    for i in lista: 
        peliculas.add(i[1].lower())
    for i in peliculas:
        cambios.append(i.capitalize())
    
    peliculas_ordenadas_sin_repetir = sorted(cambios)

    return peliculas_ordenadas_sin_repetir

def contar_aciertos_y_totales():
    """Se obtienen la cantidad de aciertos del usuario y la cantidad de frases jugadas.
    
    Argumentos:
    No tiene.
    
    Returns:
    tupla: contiene la cantidad de aciertos y frases jugadas."""

    cant_aciertos = 0
    cant_frases = 0

    with open("data/jugadores.txt", "r") as archi:
        for fila in archi:
            nombre, aciertos, total, fecha = fila.strip().split(",")
            aciertos = int(aciertos)
            total = int(total)
            cant_aciertos += aciertos
            cant_frases += total
    
    return cant_aciertos, cant_frases