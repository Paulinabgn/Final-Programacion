from modules.configuracion import app
from flask import Flask, render_template , request, session, redirect
from modules.Controlador import Controlador
from modules.Cajon import Cajon

@app.route ('/', methods = ["GET", "POST"])
def funcion_inicio ():
    if request.method == "POST":
        session ["cantidad_de_alimentos"] = int(request.form["numero_de_alimento"])
        return redirect ("/resultados")
    else:
        # Inicializa la cantidad de alimentos en la sesión si no está presente
        if "cantidad_de_alimentos" not in session:
            session["cantidad_de_alimentos"] = 0
        return render_template('inicio.html')

@app.route('/resultados')
def funcion_resultados():
    cant_alimentos = int (session["cantidad_de_alimentos"])
    cajon = Cajon ()
    controlador = Controlador (cant_alimentos)
    controlador.llenar_cajon (cajon)
    dicc = controlador.calcular_resultados (cajon)
    mensaje_de_advertencia = controlador.alertar (dicc)
    return render_template ("resultados.html", dicc = dicc, mensaje_de_advertencia = mensaje_de_advertencia)


if __name__ == "__main__":
    app.run(debug = True , host = "0.0.0.0")
