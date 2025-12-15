from abc import ABC, abstractmethod
import os
from fpdf import FPDF
from jinja2 import Environment, FileSystemLoader


class Reporte(ABC):
    def __init__(self, analitica, departamento):
        self.analitica = analitica
        self.departamento = departamento

    @abstractmethod
    def generar_reporte(self):
        pass

class ReporteHTML(Reporte):
    def generar_reporte(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('reporte.html')
        #usamos los valores y diagramas calculados/generados en Analitica
        ruta_circular = os.path.basename(self.analitica.ruta_diagrama_circular) if self.analitica.ruta_diagrama_circular else ""
        ruta_nube = os.path.basename(self.analitica.ruta_diagrama_nube_palabras) if self.analitica.ruta_diagrama_nube_palabras else ""

        html_content = template.render(
            reclamos=self.analitica.reclamos,
            departamento=self.departamento,
            num_reclamos=self.analitica.numero_de_reclamos,
            porcentajes=self.analitica.porcentaje_por_estado,
            mediana_en_proceso=self.analitica.mediana_en_proceso,
            mediana_resuelto=self.analitica.mediana_resuelto,
            ruta_circular=ruta_circular,
            ruta_nube=ruta_nube
        )

        nombre_archivo = f"reporte_{self.departamento.replace(' ', '_')}.html"
        ruta = f"./static/data/{nombre_archivo}"

        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(html_content)
        return ruta

class ReportePDF(Reporte):
    def generar_reporte(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Título del reporte
        pdf.cell(200, 10, txt=f"Reporte de Reclamos - {self.departamento}", ln=True)

        # Estadísticas, usando valores ya calulados en Analitica
        porcentajes = self.analitica.porcentaje_por_estado
        pdf.cell(0, 10, txt=f"Total de reclamos: {self.analitica.numero_de_reclamos}", ln=True)
        pdf.cell(0, 10, txt=f"Pendientes: {porcentajes['pendiente']}%", ln=True)
        pdf.cell(0, 10, txt=f"En proceso: {porcentajes['en proceso']}%", ln=True)
        pdf.cell(0, 10, txt=f"Resueltos: {porcentajes['resuelto']}%", ln=True)
        pdf.cell(0, 10, txt=f"Mediana en proceso: {self.analitica.mediana_en_proceso}", ln=True)
        pdf.cell(0, 10, txt=f"Mediana resueltos: {self.analitica.mediana_resuelto}", ln=True)

        # Gráficos
        ruta_circular = self.analitica.ruta_diagrama_circular
        ruta_nube = self.analitica.ruta_diagrama_nube_palabras
        if ruta_circular and os.path.exists(ruta_circular):
            pdf.image(ruta_circular, x=10, y=pdf.get_y(), w=90)
            pdf.ln(60)
        if ruta_nube and os.path.exists(ruta_nube):
            pdf.image(ruta_nube, x=110, y=pdf.get_y()-60, w=90)
            pdf.ln(60)

        # Lista de reclamos
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt="Listado de Reclamos:", ln=True)
        for r in self.analitica.reclamos:
            texto = f"ID: {r['id']} | Estado: {r['estado']} | {r['contenido']}"
            pdf.multi_cell(0, 10, txt=texto)

        nombre_archivo = f"reporte_{self.departamento.replace(' ', '_')}.pdf"
        ruta_pdf = f"./static/data/{nombre_archivo}"
        pdf.output(ruta_pdf)
        return ruta_pdf