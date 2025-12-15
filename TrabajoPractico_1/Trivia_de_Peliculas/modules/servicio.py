"""La capa de servicio maneja los casos de uso (las acciones que el usuario puede realizar) de la aplicación.
Coordina la interacción entre la capa de dominio y la de persistencia. 
La aplicación implementada con cualquier interfaz de usuario (web o consola) debe comunicarse solo con 
la capa de servicio es decir, solo hacer llamadas a funciones de esta capa.
"""

from modules.persistencia import generar_grafico_ejes, generar_grafico_torta, registrar_historial, obtener_frases_peliculas, obtener_historial
from modules.dominio import ordenar_peliculas, contar_aciertos_y_totales, crear_trivia, verificar_respuesta

def iniciar_trivia (archivo, n_intentos):
    info = obtener_frases_peliculas (archivo)
    juego = crear_trivia (info, n_intentos)
    return juego

def listar_peliculas (archivo):
    lista = obtener_frases_peliculas (archivo)
    n_peliculas = ordenar_peliculas (lista)
    return n_peliculas

def mostrar_resultado (nombre, intentos, exitos):
    respuesta = registrar_historial (nombre, intentos, exitos)
    return respuesta

def mostrar_historial_usuarios (archivo):
    historial = obtener_historial(archivo)
    return historial

def mostrar_grafico_eje (archivo):
    grafica_ejes = generar_grafico_ejes (archivo)
    return grafica_ejes

def mostrar_grafico_torta (archivo):
    cantidad_aciertos , cantidad_total_frases = contar_aciertos_y_totales()
    grafica_torta = generar_grafico_torta (cantidad_aciertos, cantidad_total_frases)
    return grafica_torta