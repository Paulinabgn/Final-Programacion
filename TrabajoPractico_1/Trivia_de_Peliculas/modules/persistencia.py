"""La capa de persistencia maneja el almacenamiento y recuperación de datos, por ejemplo,
usando archivos de texto. Esta capa es la que se debe modificar o reemplazar si cambio de tecnología
para almacenar los datos (por ejemplo con una base de datos). La capa de dominio no debe verse afectada
por este cambio.
"""

from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

def obtener_historial(archivo):
    """Se lee el historial de jugadores de un archivo txt y se retorna como una lista.
    
    Argumentos:
    archivo(str): nombre del archivo que contiene el historial.
    
    Returns: 
    list: lista de listas donde cada sublista contiene la info de cada jugador"""

    historial = []

    with open(archivo,"r") as archi:
        for i in archi:
            nombre, intentos, total, fecha = i.split(",")
            historial.append([nombre, intentos, total, fecha])
    
    return historial

def obtener_frases_peliculas(nombre_archivo):
    """Se obtine una lista de frases y peloculas a partir de un archivo txt.
    
    Argumentos:
    obtener_frases_peliuclas (nombre_archivo): nombre del archivo que contiene las frases y peliculas.
    
    Returns: lista de lista donde cada sublista tiene la frase y pelicula correspondiente."""

    lista = []
    with open(nombre_archivo, "r", encoding = "utf-8") as archi:
        for i in archi:
            frases, peliculas = i.rstrip().split(";")
            frases = str(frases)
            peliculas = str(peliculas)
            lista.append([frases,peliculas])
    return lista

def generar_grafico_torta (cant_aciertos, n_total_frases):
    cant_desaciertos = n_total_frases - cant_aciertos
    sizes = [cant_aciertos, cant_desaciertos]
    labels = ['Aciertos', 'Desaciertos']
    colors = ['#1aba1a', '#fc233d']

    plt.figure (figsize = (8, 6))
    plt.pie (sizes, labels = labels, colors = colors, autopct = '%1.1f%%' , startangle = 140)
    plt.title ('Grafico de torta : Aciertos vs. Desaciertos', pad = 20)
    plt.axis('equal')

    plt.savefig ("static/Diagrama de torta.pdf")
    plt.savefig ("static/Diagrama de torta.png")
    plt.close()
    return


def generar_grafico_ejes (archivo_datos):
    """Genera dos curvas en un grafico que indican la cantidad
    de aciertos en funcion de la fecha de la partida de cada
    usuario y, la cantidad de desaciertos en funcion de la fecha
    de la partida de cada usuario"""
    d_aciertos = {}
    d_desaciertos = {}

    with open (archivo_datos, "r") as archi:
        for i in archi:
            n_usuario, acierto, intento, fecha_y_hora = i.strip().split(",")
            fecha_completa, hora = fecha_y_hora.split(' ')
            dia, mes, anio = fecha_completa.split('/')
            fecha = dia + '/' + mes
            acierto = int(acierto)
            intento = int(intento)
            if fecha not in d_aciertos:
                d_aciertos [fecha] = acierto
                d_desaciertos [fecha] = intento - acierto
            else:
                d_aciertos [fecha] += acierto
                d_desaciertos [fecha] += intento - acierto
    
    plt.plot (d_aciertos.keys(), d_aciertos.values(), marker = '^' , color = 'blue' , label = 'Aciertos por día')
    plt.plot (d_desaciertos.keys(), d_desaciertos.values(), marker = 'o', color = 'red', label = 'Desaciertos por día')
    plt.legend()
    plt.savefig("static/Diagrama de lineas.pdf")
    plt.savefig("static/Diagrama de lineas.png")
    plt.close()
    return

def registrar_historial(nombre, intentos, exitos):
    """Se registra un historial de los jugadores en un archivo de texto.
    
    Argumentos:
    nombre(str): nombre del jugador.
    intentos(int): numero de intentos del jugador.
    exitos(int): numero de jugadas exitosas del jugador.
    
    Returns:
    str: info registrada del jugador."""

    fecha = datetime.now()
    fecha_hora = fecha.strftime("%d/%m/%Y %H:%M") #se formatea la hora
    registro = f"{nombre},{exitos},{intentos},{fecha_hora}\n"
    
    with open("data/jugadores.txt","a") as archi:
        archi.write(registro)
    return