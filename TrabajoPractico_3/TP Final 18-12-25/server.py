from flask import render_template, request, redirect, url_for, flash, session
from modules.config import app, login_manager
from modules.gestor_reclamos import GestorDeReclamos
from modules.gestor_usuarios import GestorDeUsuario
from modules.Formularios import FormRegistro, FormLogin, ReclamoForm
from modules.gestor_login import GestorDeLogin
from modules.factoria import crear_repositorio, obtener_personal, obtener_reclamos_similares
from modules.Analitica import Analitica
from modules.Reporte import ReporteHTML, ReportePDF
import datetime
from modules.clasificador_de_reclamos import ClasificadorDeReclamos
import nltk
import os
from flask import send_from_directory

nltk.download('punkt_tab') 

admin_list = [1]
repo_reclamo, repo_usuario = crear_repositorio()
gestor_reclamos = GestorDeReclamos(repo_reclamo)
gestor_usuarios = GestorDeUsuario(repo_usuario)
gestor_login = GestorDeLogin(gestor_usuarios, login_manager, admin_list)
clasificador = ClasificadorDeReclamos()



DEPARTAMENTOS_VALIDOS = {
    'soporte informatico': 'soporte informático',
    'soporte informático': 'soporte informático',
    'maestranza': 'maestranza',
    'secretaria tecnica': 'secretaría técnica',
    'secretaría tecnica': 'secretaría técnica'
}


RUTA = "./data/"
archivo_pesonal = RUTA+"personal.txt"
usuarios_cargados = obtener_personal(archivo_pesonal)

for usuario in usuarios_cargados:
    usuario_existente = gestor_usuarios.autenticar_usuario({"email": usuario['email'], "password": usuario['password']})
    if usuario_existente is None:
        gestor_usuarios.registrar_nuevo_usuario(
            usuario['nombre'],
            usuario['apellido'],
            usuario['email'],
            usuario['username'],
            usuario['claustro'],
            usuario['password'],
            usuario['rol'],
            usuario['departamento']
        )
    

# Rutas
@app.route("/")
def inicio():
    if 'username' in session and gestor_login.usuario_autenticado:
        username = session['username']
        rol = gestor_login.rol_usuario_actual       
    else:
        username = 'Invitado' 
        rol = ''

    session['counter'] = gestor_reclamos.numero_reclamos
    return render_template("inicio.html", user=username,logged_in=gestor_login.usuario_autenticado,rol=rol)

@app.route("/register", methods= ["GET", "POST"])
def register():
    form = FormRegistro()
    if form.validate_on_submit():
        usuario_existente = gestor_usuarios.autenticar_usuario({"email": form.email.data, "password": form.password.data})
        if usuario_existente is not None:
            flash("El usuario ya existe. Por favor, inicie sesión.")
            return redirect(url_for("login"))
        
        rol = 'usuario_final'
        gestor_usuarios.registrar_nuevo_usuario(
            form.nombre.data,
            form.apellido.data,
            form.email.data,
            form.username.data, 
            form.claustro.data,
            form.password.data,
            rol
        )
        flash("Usuario registrado con éxito.")
        return redirect(url_for("login"))
    return render_template('register.html', form=form)

@app.route("/login", methods= ["GET", "POST"])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        usuario = gestor_usuarios.autenticar_usuario({"email": form.email.data, "password": form.password.data})
        if usuario is None:
            flash("Email o contraseña incorrectos. Intente nuevamente.")
            return render_template('login.html', form=form)
        else:
            gestor_login.login_usuario(usuario)
            session['username'] = gestor_login.nombre_usuario_actual
            return redirect(url_for('inicio', user=session['username'])) 
        
    return render_template('login.html', form=form)

@app.route("/listar/", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def listar(): 
    if request.args.get('adherirse') == 'True':
        id_reclamo = request.args.get('id') #se puede poner, para evitar error, id_reclamo = int(request.args.get('id'))
        gestor_usuarios.registrar_reclamo_a_seguir(gestor_login.id_usuario_actual, id_reclamo)
        flash("Se ha adherido al reclamo con éxito")
        #return redirect(url_for('listar'))
    
    reclamos_seguidos = gestor_reclamos.filtrar_reclamos_seguidos_por_usuario(gestor_login.id_usuario_actual)
    reclamos_existentes = gestor_reclamos.listar_reclamos_existentes()
    cant_usuarios_adheridos = {reclamo['id']: gestor_usuarios.obtener_cantidad_de_usuarios_adheridos(reclamo['id']) for reclamo in reclamos_existentes}

    return render_template("listar.html", 
                           vacio= (len(reclamos_existentes) == 0), 
                           user=gestor_login.nombre_usuario_actual, 
                           user_id=gestor_login.id_usuario_actual,
                           lista_reclamos = reclamos_existentes, 
                           reclamos_seguidos = reclamos_seguidos,
                           admin = gestor_login.es_admin,
                           adherentes=cant_usuarios_adheridos)

@app.route("/misreclamos/", methods=['GET','POST'])
@gestor_login.se_requiere_login
def mis_reclamos():
    reclamos_del_usuario = gestor_reclamos.filtrar_reclamos_seguidos_por_usuario(gestor_login.id_usuario_actual)
    return render_template('mis_reclamos.html',vacio= (len(reclamos_del_usuario) == 0), 
                           user=gestor_login.nombre_usuario_actual, 
                           reclamos_seguidos = reclamos_del_usuario,
                           admin = gestor_login.es_admin)


@app.route("/reclamo_soporte_informatico", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def reclamo_soporte_informatico():

    if request.args.get('adherirse') == 'True':
        id_reclamo = request.args.get('id') #para evitar errores y que sea entero, se puede poner id_reclamo = int(request.args.get('id')) --> lo mismo para maestranza y secretaria_tecnica
        gestor_usuarios.registrar_reclamo_a_seguir(gestor_login.id_usuario_actual, id_reclamo)
        flash("Se ha adherido al reclamo con éxito")
        #para evitar que al refrescar el usuario se adhiera al mismo reclamo, agregar: return redirect(url_for('reclamo_soporte_informatico')) --> lo mismo para maestranza y secretaria_tecnica
    reclamos_seguidos = gestor_reclamos.filtrar_reclamos_seguidos_por_usuario(gestor_login.id_usuario_actual)
    
    reclamos_existentes = gestor_reclamos.filtrar_reclamos_por_depto('soporte informático')

    cant_usuarios_adheridos = {reclamo['id']: gestor_usuarios.obtener_cantidad_de_usuarios_adheridos(reclamo['id']) for reclamo in reclamos_existentes}

    return render_template("reclamo_soporte_informatico.html", 
                           vacio= (len(reclamos_existentes) == 0), 
                           user=gestor_login.nombre_usuario_actual, 
                           lista_reclamos = reclamos_existentes, 
                           reclamos_seguidos = reclamos_seguidos,
                           admin = gestor_login.es_admin,
                           adherentes=cant_usuarios_adheridos)

@app.route("/reclamo_maestranza", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def reclamo_maestranza():

    if request.args.get('adherirse') == 'True':
        id_reclamo = request.args.get('id')
        gestor_usuarios.registrar_reclamo_a_seguir(gestor_login.id_usuario_actual, id_reclamo)
        flash("Se ha adherido al reclamo con éxito")
    
    reclamos_seguidos = gestor_reclamos.filtrar_reclamos_seguidos_por_usuario(gestor_login.id_usuario_actual)
    
    reclamos_existentes = gestor_reclamos.filtrar_reclamos_por_depto('maestranza')

    cant_usuario_adheridos = {reclamo['id']: gestor_usuarios.obtener_cantidad_de_usuarios_adheridos(reclamo['id']) for reclamo in reclamos_existentes}

    return render_template("reclamo_maestranza.html", 
                           vacio= (len(reclamos_existentes) == 0), 
                           user=gestor_login.nombre_usuario_actual, 
                           lista_reclamos = reclamos_existentes, 
                           reclamos_seguidos = reclamos_seguidos,
                           admin = gestor_login.es_admin,
                           adherentes=cant_usuario_adheridos)
    
@app.route("/reclamo_secretaria_tecnica", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def reclamo_secretaria_tecnica():

    if request.args.get('adherirse') == 'True':
        id_reclamo = request.args.get('id')
        gestor_usuarios.registrar_reclamo_a_seguir(gestor_login.id_usuario_actual, id_reclamo)
        flash("Se ha adherido al reclamo con éxito")
    
    reclamos_seguidos = gestor_reclamos.filtrar_reclamos_seguidos_por_usuario(gestor_login.id_usuario_actual)
    
    reclamos_existentes = gestor_reclamos.filtrar_reclamos_por_depto('secretaría técnica')

    cant_usuarios_adheridos = {reclamo['id']: gestor_usuarios.obtener_cantidad_de_usuarios_adheridos(reclamo['id']) for reclamo in reclamos_existentes}

    return render_template("reclamo_secretaria_tecnica.html", 
                           vacio= (len(reclamos_existentes) == 0), 
                           user=gestor_login.nombre_usuario_actual, 
                           lista_reclamos = reclamos_existentes, 
                           reclamos_seguidos = reclamos_seguidos,
                           admin = gestor_login.es_admin,
                           adherentes=cant_usuarios_adheridos)
    
@app.route("/agregar_reclamo", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def agregar_reclamo():
    form = ReclamoForm()
    if form.validate_on_submit():
        contenido = form.contenido.data
        ruta_imagen = None
        if form.imagen.data and form.imagen.data.filename:
            import os
            os.makedirs("./data/imagenes", exist_ok=True)
            ruta_imagen = f"./data/imagenes/{form.imagen.data.filename}"
            form.imagen.data.save(ruta_imagen)
        session ['contenido'] = contenido
        session['ruta_imagen'] = ruta_imagen
        reclamos_similares = obtener_reclamos_similares(contenido, gestor_reclamos.listar_reclamos_existentes())
        vacio = len(reclamos_similares) == 0
        if vacio:
            # Si no hay similares, crea el reclamo directamente y redirige
            rec = [contenido]
            depto = clasificador.clasificar(rec)[0]
            depto = DEPARTAMENTOS_VALIDOS.get(depto.lower().strip(), depto)
            fecha_y_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            try:
                tiempo=int(form.tiempo_de_resolucion.data) if hasattr(form, "tiempo_de_resolucion") else 1
            except (TypeError, ValueError):
                tiempo=1
            if tiempo < 1:
                tiempo = 1
            elif tiempo > 15:
                tiempo = 15
            gestor_reclamos.agregar_nuevo_reclamo('pendiente', contenido, depto, gestor_login.id_usuario_actual, fecha_y_hora, ruta_imagen, tiempo_de_resolucion=tiempo)
            id_reclamo = gestor_reclamos.filtrar_reclamo_por_contenido(contenido)['id']
            gestor_usuarios.registrar_reclamo_a_seguir(gestor_login.id_usuario_actual, id_reclamo)
            flash("Reclamo creado con éxito")
            return redirect(url_for("listar"))
        else:
            # Si hay similares, muestra la página de confirmación
            return render_template("reclamar.html", vacio=vacio, reclamos_similares=reclamos_similares)
    return render_template("agregar.html", form=form)

@app.route("/confirmar_reclamo", methods=['POST'])
@gestor_login.se_requiere_login
def confirmar_reclamo():
    contenido = session.get('contenido')
    ruta_imagen = session.get('ruta_imagen')
    rec = [contenido]
    depto = clasificador.clasificar(rec)[0]
    depto = DEPARTAMENTOS_VALIDOS.get(depto.lower().strip(), depto)
    fecha_y_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    try:
        tiempo = int(session.get('tiempo_de_resolucion', 1))
    except (TypeError, ValueError):
        tiempo = 1
    if tiempo < 1:
        tiempo = 1
    if tiempo > 15:
        tiempo = 15
    gestor_reclamos.agregar_nuevo_reclamo('pendiente', contenido, depto, gestor_login.id_usuario_actual, fecha_y_hora, ruta_imagen, tiempo_de_resolucion=tiempo)
    id_reclamo = gestor_reclamos.filtrar_reclamo_por_contenido(contenido)['id']
    gestor_usuarios.registrar_reclamo_a_seguir(gestor_login.id_usuario_actual, id_reclamo)
    flash("Reclamo creado con éxito")
    return redirect(url_for("listar"))


#ADMIN PAGES------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/manejar_reclamos", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def manejar_reclamos():
    departamento_usuario = gestor_usuarios.obtener_usuario(gestor_login.id_usuario_actual)['departamento']
    rol = gestor_usuarios.obtener_usuario(gestor_login.id_usuario_actual)['rol']

    reclamos_existentes = gestor_reclamos.filtrar_reclamos_por_depto(departamento_usuario)

    #username del creador
    creadores = {r['id']: gestor_usuarios.obtener_usuario(r['id_usuario'])['username'] for r in reclamos_existentes}

    #lista de usernames adheridos
    adherentes_usernames = {}
    for r in reclamos_existentes:
        adheridos_ids = gestor_usuarios.obtener_usuarios_adheridos_al_reclamo(r['id'])
        adherentes_usernames[r['id']] = [gestor_usuarios.obtener_usuario(id)['username'] for id in adheridos_ids]

    if request.method == "POST": 
        id_reclamo = request.form.get("reclamo_id")
        nuevo_estado = request.form.get("estado")
        tiempo_de_resolucion = request.form.get("tiempo_de_resolucion")
        print(tiempo_de_resolucion)
        nuevo_depto = request.form.get("departamento")

        if nuevo_estado == "en proceso":
                try:
                    tiempo_de_resolucion = int(tiempo_de_resolucion)
                except (TypeError, ValueError):
                    tiempo_de_resolucion = 1
                if tiempo_de_resolucion < 1:
                    tiempo_de_resolucion = 1
                elif tiempo_de_resolucion > 15:
                    tiempo_de_resolucion = 15
                gestor_reclamos.cambiar_estado_reclamo(id_reclamo, nuevo_estado, tiempo_de_resolucion)
        
        elif nuevo_estado == "resuelto" or nuevo_estado == "invalido":
            reclamo_actual = gestor_reclamos.devolver_reclamo(id_reclamo)
            fecha_y_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            fecha_y_hora_inicio = reclamo_actual.get('fecha_hora')
            fecha_inicio = datetime.datetime.strptime(fecha_y_hora_inicio, "%d/%m/%Y %H:%M")
            fecha_fin = datetime.datetime.strptime(fecha_y_hora_actual, "%d/%m/%Y %H:%M")
            dias_transcurridos = (fecha_fin - fecha_inicio).days
            tiempo_actual = dias_transcurridos if dias_transcurridos > 0 else 1
            try:
                tiempo_actual = int(tiempo_actual)
            except (TypeError, ValueError):
                tiempo_actual = 1
            if tiempo_actual < 1:
                tiempo_actual = 1
            elif tiempo_actual > 15:
                tiempo_actual = 15
            gestor_reclamos.cambiar_estado_reclamo(id_reclamo, nuevo_estado, tiempo_actual)

        if nuevo_depto in ["secretaría técnica", "maestranza", "soporte informático"]:
            gestor_reclamos.derivar(id_reclamo, nuevo_depto)
        
        return redirect(url_for('manejar_reclamos'))

    return render_template("manejar_reclamos.html", 
                           rol=rol,
                           reclamos_existentes=reclamos_existentes,
                           vacio=len(reclamos_existentes)==0,
                           adherentes=adherentes_usernames,
                           creadores=creadores,
                           departamento=departamento_usuario)

@app.route("/derivar", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def derivar():
    
    edit_form = ReclamoForm()
    if request.method == 'POST':
        try:
            gestor_reclamos.derivar(int(edit_form.id.data), 
                                    edit_form.departamento.data)
        except ValueError as e:
            flash(str(e))
        else:
            flash("Estado cambiado con éxito")
            return redirect(url_for('listar'))


@app.route("/analitica/", methods=["GET", "POST"])
@gestor_login.se_requiere_login
def analitica():
    usuario = gestor_usuarios.obtener_usuario(gestor_login.id_usuario_actual)
    departamento = usuario['departamento']

    # Filtra los reclamos por departamento
    lista_reclamos = gestor_reclamos.filtrar_reclamos_por_depto(departamento)
    if not lista_reclamos or len(lista_reclamos) == 0:
        return render_template("sin_reclamos.html", departamento=departamento)
    analitica = Analitica(lista_reclamos,departamento=departamento)

    return render_template(
        "analitica.html",
        num_reclamos=analitica.numero_de_reclamos,
        porcentajes=analitica.porcentaje_por_estado,
        mediana_en_proceso=analitica.mediana_en_proceso,
        mediana_resuelto=analitica.mediana_resuelto,
        ruta_circular=os.path.basename(analitica.ruta_diagrama_circular) if analitica.ruta_diagrama_circular else "",
        ruta_nube=os.path.basename(analitica.ruta_diagrama_nube_palabras) if analitica.ruta_diagrama_nube_palabras else "",
        departamento=departamento
    )


@app.route("/generar_reporte", methods=["GET"])
@gestor_login.se_requiere_login
def generar_reporte():
    formato = request.args.get("formato", "html").lower()
    usuario = gestor_usuarios.obtener_usuario(gestor_login.id_usuario_actual)
    departamento = usuario['departamento']

    reclamos = gestor_reclamos.filtrar_reclamos_por_depto(departamento)
    if not reclamos or len(reclamos) == 0:
        return render_template("sin_reclamos.html", departamento=departamento)
    
    analitica = Analitica(reclamos, departamento)

    # Crea la carpeta static/data si no existe
    os.makedirs("static/data", exist_ok=True)

    if formato == "pdf":
        reporte = ReportePDF(analitica, departamento)
        ruta = reporte.generar_reporte()
        nombre_archivo = os.path.basename(ruta)
        return redirect(url_for('static', filename=f"data/{nombre_archivo}"))  
    else:
        # reporte = ReporteHTML(analitica, departamento)
        # ruta = reporte.generar_reporte()
        # with open(ruta, "r", encoding="utf-8") as f:
        #     html_content = f.read()
        # return html_content
        # nombre_archivo = os.path.basename(ruta)
        return render_template("reporte.html",
                                reclamos=analitica.reclamos,
                                departamento=departamento,
                                numero_de_reclamos=analitica.numero_de_reclamos,
                                porcentajes=analitica.porcentaje_por_estado,
                                mediana_en_proceso=analitica.mediana_en_proceso,
                                mediana_resuelto=analitica.mediana_resuelto,
                                ruta_circular=os.path.basename(analitica.ruta_diagrama_circular) if analitica.ruta_diagrama_circular else "",
                                ruta_nube=os.path.basename(analitica.ruta_diagrama_nube_palabras) if analitica.ruta_diagrama_nube_palabras else "",
                                )


@app.route("/descargar_reporte_html")
@gestor_login.se_requiere_login
def descargar_reporte_html():
    usuario = gestor_usuarios.obtener_usuario(gestor_login.id_usuario_actual)
    departamento = usuario['departamento']
    reclamos = gestor_reclamos.filtrar_reclamos_por_depto(departamento)
    if not reclamos or len(reclamos) == 0:
        return render_template("sin_reclamos.html", departamento=departamento)
    analitica = Analitica(reclamos, departamento)
    reporte = ReporteHTML(analitica, departamento)
    ruta = reporte.generar_reporte()
    nombre_archivo = os.path.basename(ruta)
    return send_from_directory("static/data", nombre_archivo, as_attachment=True)

@app.route("/ayuda", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def ayuda():
    return render_template("ayuda.html")

@app.route("/logout",methods=['POST'])
def logout():
    gestor_login.logout_usuario()
    session['username'] = 'Invitado'
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')