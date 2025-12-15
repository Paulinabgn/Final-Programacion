# Aplicación principal
from modules.configuracion import app 
from flask import render_template, request, redirect, url_for, session, send_file
from modules.servicio import iniciar_trivia, listar_peliculas, mostrar_resultado, mostrar_historial_usuarios, mostrar_grafico_eje, mostrar_grafico_torta

archivo = "data/frases_de_peliculas.txt"
#info = obtener_frases_peliculas (archivo)

@app.route ("/", methods = ["GET", "POST"])
def funcion_inicio ():
    if request.method == "POST":
        session ["cantidad_frases"] = int (request.form["numero_de_frases"])
        session ["usuario"] = request.form ["nombre_de_usuario"]
        session ["contador"] = 0
        session ["trivia"] = iniciar_trivia (archivo, session["cantidad_frases"])  # Almacenar la trivia en la sesión
        session ["correcta"] = False
        session ["boton_clik"] = False
        session ["contador_aciertos"] = 0
        session ["contador_fallos"] = 0
        return redirect(url_for("funcion_juego"))
    return render_template("inicio.html")


@app.route ("/juego", methods = ["GET", "POST"])
def funcion_juego():
    if "trivia" in session:
        trivia = session ["trivia"]  
        contador = session ["contador"]
        if session ["contador"] < session["cantidad_frases"]:
            if request.method == "POST":
                session ["opcion_elegida"] = request.form ["respuesta"]
                pelicula_correcta = trivia [contador]["pelicula_correcta"]
                
                if session ["opcion_elegida"] ==  pelicula_correcta:
                    session ["correcta"] = True
                    session ["contador_aciertos"]+=1

                else:
                    session ["correcta"] = False
                    session ["contador_fallos"]+=1
                session ["contador"] += 1
                
                return redirect(url_for("funcion_resultado_ind"))  # Redirigir a la página de resultado individual
            
            # Cargar la información de la siguiente pregunta desde la sesión
            siguiente_pregunta = trivia [contador]
            frase = siguiente_pregunta ["frase"]
            opciones = siguiente_pregunta ["opciones"]
            return render_template("juego.html", frase = frase, opciones = opciones)
        mostrar_resultado (session ["usuario"], session ["cantidad_frases"], session ["contador_aciertos"])
        
    return render_template("puntaje_final_ind.html", cantidad_frases = session ["cantidad_frases"], usuario = session ['usuario'], contador_aciertos = session ["contador_aciertos"] )


@app.route("/resultado_ind", methods = ["GET", "POST"])
def funcion_resultado_ind():
    if "trivia" in session:
        trivia = session ["trivia"]
        contador = session ["contador"]
        pelicula_correcta = trivia [contador-1]["pelicula_correcta"]  
        return render_template("resultado_ind.html", respuesta_correcta = session ["correcta"], correcta = pelicula_correcta, contador = session ["contador_aciertos"], cantidad_frases = session ["cantidad_frases"])    
    return redirect(url_for("funcion_inicio"))

@app.route("/resultado_individual_final", methods = ["GET", "POST"])
def funcion_resultado_ind_final ():
    if request.method == "POST":
        return render_template("puntaje_final_ind.html", cantidad_frases = session ["cantidad_frases"], usuario = session ["usuario"], contador_aciertos = session ["correcta"] )



@app.route("/listado", methods = ["GET","POST"])
def funcion_listado():
    if request.method == "POST":
        listado = listar_peliculas (archivo)
        return render_template("listado.html", peliculas = listado)
    else:
        listado = listar_peliculas (archivo)
        return render_template("listado.html", peliculas = listado)
    
@app.route("/resultado", methods = ["GET","POST"])
def funcion_resultados():
    if request.method == "POST":
        historial = mostrar_historial_usuarios ("data/jugadores.txt")
        return render_template("resultados.html", resultados = historial) 
    else:
        historial = mostrar_historial_usuarios ("data/jugadores.txt")
        return render_template ("resultados.html", resultados = historial)    

@app.route ("/historial", methods=["GET", "POST"])
def funcion_historial ():
    if request.method == "GET":
        historial = mostrar_historial_usuarios ("data/jugadores.txt")
        return render_template("historial.html", resultados = historial)
    else:
        historial = mostrar_historial_usuarios ("data/jugadores.txt")
        return render_template ("historial.html", resultados = historial)  

@app.route("/grafico_lineal", methods = ["GET","POST"])
def funcion_grafico_lineal():
    if request.method == "GET":
        diagrama = mostrar_grafico_eje ("data/jugadores.txt")
        return render_template("grafica_lineal.html", diagrama = diagrama)

    
@app.route("/grafico_torta", methods = ["GET","POST"])
def funcion_grafico_torta():
    if request.method == "GET":
        grafico_base64 = mostrar_grafico_torta ("data/jugadores.txt")
        return render_template ("grafica_torta.html", grafico_base64 = grafico_base64)

if __name__=="__main__":
    app.run(debug = True , host = "0.0.0.0") 