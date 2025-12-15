from modules.Monticulos import MonticuloMediana
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg'
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from collections import Counter
import os
try:
    stopwords.words('spanish')
except LookupError:
    nltk.download('stopwords')


class Analitica:
    
    def __init__ (self, lista_reclamos, departamento=None):
        self.reclamos = lista_reclamos  # cada reclamo es un dict con al menos 'estado', 'contenido', 'tiempo_de_resolucion'
        #nltk.download('stopwords', quiet=True) # TODO: sacar descarga de aquí
        self.stopwords = set(stopwords.words('spanish')) #filtro de palabras comunes
        self.__monticulo_med = MonticuloMediana()
        self.departamento = departamento
        self.numero_de_reclamos = self.calcular_numero_de_reclamos()
        self.porcentaje_por_estado = self.calcular_porcentajes_estados()
        self.mediana_en_proceso = self.calcular_mediana_por_estado('en proceso')
        self.mediana_resuelto = self.calcular_mediana_por_estado('resuelto')
        self.ruta_diagrama_circular = self.generar_diagrama_circular()
        self.ruta_diagrama_nube_palabras = self.generar_nube_de_palabras()

    def calcular_numero_de_reclamos(self):
        return len(self.reclamos)

    def calcular_porcentajes_estados(self):
        total = len(self.reclamos)
        contador = {'pendiente': 0, 'en proceso': 0, 'resuelto': 0}
        for r in self.reclamos:
            estado = r.get('estado', '').lower()
            if estado in contador:
                contador[estado] += 1
        porcentajes = {}
        for e in contador:
            if total > 0:
                porcentajes[e] = contador[e] * 100 / total
            else:
                porcentajes[e] = 0
        return porcentajes

    def calcular_mediana_por_estado(self, estado_objetivo):
        self.__monticulo_med = MonticuloMediana() #lo reinicia para cada calculo
        for r in self.reclamos:
            if r.get('estado', '').lower() == estado_objetivo and r.get('tiempo_de_resolucion') is not None:
                self.__monticulo_med.agregar_dato(r['tiempo_de_resolucion'])
        return self.__monticulo_med.calcular_mediana()


    def generar_diagrama_circular(self):

        porcentajes = self.porcentaje_por_estado
        etiquetas = list(porcentajes.keys())
        valores = [porcentajes[e] for e in etiquetas]
        
        plt.figure(figsize=(6,6))
        if sum(valores) == 0:
            plt.text(0.5, 0.5, 'No hay reclamos\npendientes, en proceso\no resueltos', 
                    horizontalalignment='center', 
                    verticalalignment='center',
                    transform=plt.gca().transAxes,
                    fontsize=14,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
            plt.axis('off')  # Ocultar ejes
        else:
            plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
            
        plt.title(f'Reclamos por departamento (Total: {self.calcular_numero_de_reclamos()})')
        plt.axis('equal')
        nombre_archivo = f"static/diagrama_circular_{self.departamento.replace(' ', '_')}.png" 
        plt.savefig(nombre_archivo)
        plt.close()
        return nombre_archivo


    def generar_nube_de_palabras(self):
        if not self.departamento:
            return None
        todos_los_contenidos = ' '.join(r.get('contenido', '') for r in self.reclamos)
        palabras = [p.lower() for p in todos_los_contenidos.split() if p.lower() not in self.stopwords and p.isalpha()]
        conteo = Counter(palabras)
        palabras_frecuentes = dict(conteo.most_common(15))
        if not palabras_frecuentes:
            return None
        wc = WordCloud(width=800, height=400, background_color='white')
        wc.generate_from_frequencies(palabras_frecuentes)
        plt.figure(figsize=(10,5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title("Nube de Palabras Clave en Reclamos")
        nombre_archivo = f"static/nube_palabras_{self.departamento.replace(' ', '_')}.png"
        plt.savefig(nombre_archivo)
        plt.close()
        return nombre_archivo



