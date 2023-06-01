from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL, MySQLdb
import pymysql

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sesion')
def homedd():
    return render_template('sesion.html')


@app.route('/prueba')
def admin():
    return render_template('prueba.html')

@app.route('/vacantes_publicacion')
def adminemofmvomsv():
    return render_template('vacantes_publicacion.html')


@app.route('/acceso-login', methods=["GET", "POST"])
def login():
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form:
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s', (_correo, _password,))
        account = cur.fetchone()

        if account:
            session['logueado'] = True
            session['id'] = account['id']
            return render_template("layout.html")
        else:
            return render_template('sesion.html', mensaje="")


@app.route('/layout')
def layout():
    return render_template("layout.html")


@app.route('/bolsa')
def bolsa():
    return render_template("bolsa.html")


@app.route('/productos')
def productos():
    return render_template("productos.html")


@app.route('/ropa')
def ropa():
    return render_template("ropa.html")


@app.route('/accesorios')
def accesorios():
    return render_template("accesorios.html")


@app.route('/refacciones')
def refacciones():
    return render_template("refacciones.html")


"inicio de base de datos"

"AREA EDITAR"

@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", comentarios = datos)

@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
    dato  = cursor.fetchall()
    return render_template("area_edi.html", comentar =dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

"CARRERA EDITAR"

@app.route('/carrera')
def carrera1():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
    datos = cursor.fetchall()
    return render_template("carrera.html", comentarios = datos)

@app.route('/carrera_editar/<string:id>')
def carrera1_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera where idCarrera = %s', (id))
    dato  = cursor.fetchall()
    return render_template("carrera_edi.html", comentar =dato[0])

@app.route('/carrera_fedita/<string:id>',methods=['POST'])
def carrera1_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update carrera set descripcion=%s where idCarrera=%s', (desc,id))
        conn.commit()
    return redirect(url_for('carrera'))


"ESCOLARIDAD EDITAR"

@app.route('/escolaridad')
def escolaridad1():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", comentarios = datos)

@app.route('/escolaridad_editar/<string:id>')
def escolaridad1_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad where idEscolaridad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("escolaridad_edi.html", comentar =dato[0])

@app.route('/escolaridad_fedita/<string:id>',methods=['POST'])
def escolaridad1_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update escolaridad set descripcion=%s where idEscolaridad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('escolaridad'))

"ESTADOCIVIL EDITAR"

@app.route('/estadocivil')
def estadocivil1():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil order by idEstadoCivil')
    datos = cursor.fetchall()
    return render_template("estadocivil.html", comentarios = datos)

@app.route('/estadocivil_editar/<string:id>')
def estadocivil1_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil where idEstadoCivil = %s', (id))
    dato  = cursor.fetchall()
    return render_template("estadocivil_edi.html", comentar =dato[0])

@app.route('/estadocivil_fedita/<string:id>',methods=['POST'])
def estadocivil1_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update estado_civil set descripcion=%s where idEstadoCivil=%s', (desc,id))
        conn.commit()
    return redirect(url_for('estadocivil'))

"GRADOAVANCE EDITAR"

@app.route('/gradoavance')
def gradoavance1():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance order by idGradoAvance')
    datos = cursor.fetchall()
    return render_template("gradoavance.html", comentarios = datos)

@app.route('/gradoavance_editar/<string:id>')
def gradoavance1_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance where idGradoAvance = %s', (id))
    dato  = cursor.fetchall()
    return render_template("gradoavance_edi.html", comentar =dato[0])

@app.route('/gradoavance_fedita/<string:id>',methods=['POST'])
def gradoavance1_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update grado_avance set descripcion=%s where idGradoAvance=%s', (desc,id))
        conn.commit()
    return redirect(url_for('gradoavance'))


"HABILIDADES EDITAR"

@app.route('/habilidad')
def habilidad1():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template("habilidad.html", comentarios = datos)

@app.route('/habilidad_editar/<string:id>')
def habilidad1_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("habilidad_edi.html", comentar =dato[0])

@app.route('/habilidad_fedita/<string:id>',methods=['POST'])
def habilidad1_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('habilidad'))

"IDIOMAS EDITAR"

@app.route('/idioma')
def idioma1():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", comentarios = datos)

@app.route('/idioma_editar/<string:id>')
def idioma1_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma where idIdioma = %s', (id))
    dato  = cursor.fetchall()
    return render_template("idioma_edi.html", comentar =dato[0])

@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma1_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcion=%s where idIdioma=%s', (desc,id))
        conn.commit()
    return redirect(url_for('idioma'))


@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))

"Catalogo vacantes"

@app.route('/vacante')
def vacante():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idVacantess, descripcion from vacante order by idVacantess')
    datos = cursor.fetchall()
    return render_template("vacante.html", comentarios = datos)


@app.route('/vacante')
def hadsdasdas():
    return render_template("vacante.html")

"Catalogo publicado"

@app.route('/publicado')
def publicado():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPublicado, descripcion from publicado order by idPublicado')
    datos = cursor.fetchall()

    return render_template("publicado.html", comentarios = datos,  catArea = '   ')


"PAGINAS"
@app.route('/publicacion')
def publicacion():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT  idrequisicion, folio,puesto_cubrir FROM agregar_requisicion where estado=1 ORDER BY idrequisicion')
    datos = cursor.fetchall()
    conn.close()

    return render_template("publicacion.html", comentarios=datos, dat='   ', catArea = '   ',  catAreas = '   ')

@app.route('/publicacion_llenar')
def requisicion_publicacion_llenar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idPublicado, descripcion from publicado ')
    datos6 = cursor.fetchall()

    return render_template("publicacion_llenar.html", catArea=datos1, catAreas=datos6)

"Catalogo estado civil"

@app.route('/estadocivil')
def estadocivil():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil order by idEstadoCivil')
    datos = cursor.fetchall()
    return render_template("estadocivil.html", comentarios = datos)

@app.route('/estadocivil_borrar/<string:id>')
def estadpcivil_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from estado_civil where idEstadoCivil= {0}'.format(id))
    conn.commit()
    return redirect(url_for('estadocivil'))

@app.route('/estadocivil_agregar')
def estadocivil_agregar():
    return render_template("estadocivil_agregar.html")

@app.route('/estadocivil_fagrega', methods=['POST'])
def estadocivil_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into estado_civil (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('estadocivil'))


"catalogo Escolaridad"

@app.route('/escolaridad')
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", comentarios = datos)

@app.route('/escolaridad_borrar/<string:id>')
def escolaridad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from escolaridad where idEscolaridad= {0}'.format(id))
    conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/escolaridad_agregar')
def escolaridad_agregar():
    return render_template("escolaridad_agregar.html")

@app.route('/escolaridad_fagrega', methods=['POST'])
def escolaridad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into escolaridad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('escolaridad'))

"Catalogo carrera"

@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
    datos = cursor.fetchall()
    return render_template("carrera.html", comentarios = datos)

@app.route('/carrera_borrar/<string:id>')
def carrera_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from carrera where idCarrera= {0}'.format(id))
    conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_agregar')
def carrera_agregar():
    return render_template("carrera_agregar.html")


@app.route('/carrera_fagrega', methods=['POST'])
def carrera_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into carrera (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('carrera'))


"Catalogo Grado Avance"

@app.route('/gradoavance')
def gradoavance():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance order by idGradoAvance')
    datos = cursor.fetchall()
    return render_template("gradoavance.html", comentarios = datos)

@app.route('/gradoavance_borrar/<string:id>')
def gradoavance_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from grado_avance where idGradoAvance= {0}'.format(id))
    conn.commit()
    return redirect(url_for('gradoavance'))

@app.route('/gradoavance_agregar')
def gradoavance_agregar():
    return render_template("gradoavance_agregar.html")


@app.route('/gradoavance_fagrega', methods=['POST'])
def gradoavance_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into grado_avance (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('gradoavance'))

"Catalogo idioma"

@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", comentarios = datos)

@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma= {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template("idioma_agregar.html")


@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into idioma (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('idioma'))

"Catalogo habilidad"

@app.route('/habilidad')
def habilidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template("habilidad.html", comentarios = datos)

@app.route('/habilidad_borrar/<string:id>')
def habilidad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad= {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_agregar')
def habilidad_agregar():
    return render_template("habilidad_agregar.html")


@app.route('/habilidad_fagrega', methods=['POST'])
def habilidad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('habilidad'))


"Puesto"
@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("puesto.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')


@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))


@app.route('/puesto_agr')
def puesto_agrOp2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    return render_template("puesto_agr.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)



@app.route('/requisicion_pend')
def requisicion_pend():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT  idrequisicion, folio,puesto_cubrir FROM agregar_requisicion where estado=0 ORDER BY idrequisicion')
    datos = cursor.fetchall()
    conn.close()

    return render_template("requisicion_pend.html", comentarios=datos, dat='   ', catArea = '   ',  catAreas = '   ')


@app.route('/requisicion_agregar')
def agregar_combo():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idVacantess, descripcion from vacante ')
    datos6 = cursor.fetchall()

    return render_template("requisicion_agregar.html", catArea=datos1, catAreas=datos6)
    


@app.route('/requisicion_fagrega2', methods=['POST'])
def requisicion_fagrega2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    if request.method == 'POST':

        if  'idArea' in request.form:
                idAr = request.form['idArea']
        else:
                idAr = '1'
        
        if  'idVacantess' in request.form:
                idVa = request.form['idVacantess']
        else:
                idVa = '1'

    if request.method == 'POST':
        folio = request.form['folio']
        fecha_ela = request.form['fecha_ela']
        puesto_cubrir = request.form['puesto_cubrir']
        nombre_solicita = request.form['nombre_solicita']
        fecha_reclutamiento = request.form['fecha_reclutamiento']
        fecha_inicio_vacante = request.form['fecha_inicio_vacante']
        numerodevaca = request.form['numerodevaca']
        tipo_vacante = request.form['tipo_vacante']

        cursor.execute("INSERT INTO agregar_requisicion (idVacantess ,idArea, folio, fecha_ela, puesto_cubrir, nombre_solicita, fecha_reclutamiento,fecha_inicio_vacante,numerodevaca,tipo_vacante) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (idVa,idAr, folio, fecha_ela, puesto_cubrir, nombre_solicita, fecha_reclutamiento,fecha_inicio_vacante,numerodevaca,tipo_vacante))
        conn.commit()

    return redirect(url_for('requisicion_pend'))




@app.route('/puesto_fagrega2', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadoCivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']


    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute(
    'insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
    'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
    'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF,
     reqP, resp, conT))
    conn.commit()

    cursor.execute('select idPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato = cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh =nhab[0]+1

    for i in range(1,nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP,i))
            conn.commit()

    return redirect(url_for('puesto'))



@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos11 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s',(idP))
    datos12 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',(idP))
    datos13 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',(idP))
    datos14 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()


    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        idGA = request.form['idGradoAvance']
        idCa = request.form['idCarrera']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()

    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
            conn.commit()
    return redirect(url_for('puesto'))


@app.route('/requisicion_agregar')
def requisicion_agregar():
    return render_template("requisicion_agregar.html")

    
@app.route('/requisicion_fdetalle/<string:idr>', methods=['GET'])
def requisicion_fdetalle(idr):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT idrequisicion, folio, puesto_cubrir FROM agregar_requisicion where estado=0 ORDER BY idrequisicion')
    datos = cursor.fetchall()

    cursor.execute('SELECT idrequisicion, folio, fecha_ela, puesto_cubrir, nombre_solicita, fecha_reclutamiento, fecha_inicio_vacante, numerodevaca, tipo_vacante FROM agregar_requisicion WHERE idrequisicion = %s', (idr,))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, agregar_requisicion b where a.idArea = b.idArea and b.idrequisicion = %s', (idr,))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idVacantess, a.descripcion from vacante a, agregar_requisicion b where a.idVacantess = b.idVacantess and b.idrequisicion = %s', (idr,))
    datos6 = cursor.fetchall()

    return render_template("requisicion_pend.html", comentarios=datos, dat=dato[0], catArea=datos1[0],catAreas=datos6[0])


@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM agregar_requisicion WHERE idrequisicion = %s', (id,))
    conn.commit()
    return redirect(url_for('requisicion_pend'))


@app.route('/autorizacion_de_requisicion/<string:id>')
def requisicion_agregarefewfw(id=None):

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT idrequisicion, folio, puesto_cubrir,numerodevaca FROM agregar_requisicion WHERE idrequisicion = %s', (id))
    dato = cursor.fetchall()

    return render_template("/autorizacion_de_requisicion.html",id=id, dat=dato[0])


@app.route('/regresar/<string:id>')
def autorizacion_de_requdvmnfdhivbuvhbuhberb(id=None):

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('UPDATE agregar_requisicion SET estado = 0 WHERE idrequisicion = {0}'.format(id))
    conn.commit()
    return redirect(url_for('requisicion_pend'))

@app.route('/autorizacion_de_requisicivfvsddf/<string:id>', methods=['POST'])
@app.route('/autorizacion_de_requisicivfvsddf/<string:id>', methods=['GET','POST'])
def autorizacion_de_requisicion(id=None):

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor() 

    if request.method == 'POST':
        revisado = request.form['revisado']
        autorizado = request.form['autorizado']
        nombre_puesto = request.form['nombre_puesto']

        cursor.execute("INSERT INTO autorizacion (solicitud_puesto,revisado, autorizado, nombre_puesto) VALUES (%s, %s, %s, %s)", (id,revisado, autorizado,nombre_puesto))
        conn.commit()

        print("INSERT INTO autorizacion (revisado, autorizado, nombre_puesto) VALUES (%s, %s, %s)", (revisado, autorizado,nombre_puesto))

   
    cursor.execute('UPDATE agregar_requisicion SET estado = 1 WHERE idrequisicion = {0}'.format(id))
    conn.commit()
    
    return redirect(url_for('requisicion_autorizadas'))



@app.route('/publicacion_fdetalle/<string:idr>', methods=['GET'])
def publicacion_fdetalle(idr):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT idrequisicion, folio, puesto_cubrir FROM agregar_requisicion where estado=1 ORDER BY idrequisicion')
    datos = cursor.fetchall()

    cursor.execute('SELECT idrequisicion, folio, fecha_ela, puesto_cubrir, nombre_solicita, fecha_reclutamiento, fecha_inicio_vacante, numerodevaca, tipo_vacante FROM agregar_requisicion WHERE idrequisicion = %s', (idr,))
    dato = cursor.fetchall()


    cursor.execute('select a.idVacantess, a.descripcion from vacante a, agregar_requisicion b where a.idVacantess = b.idVacantess and b.idrequisicion = %s', (idr,))
    datos6 = cursor.fetchall()

    return render_template("publicacion.html", comentarios=datos, dat=dato[0],catAreas=datos6[0])


"Guardar datos de Publicacion llenar"

@app.route('/publicacion_fagregar', methods=['POST'])
def publicacion_fagregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        idPublicado = request.form['idPublicado']
        fecha_inicio_publicacion = request.form['fecha_inicio_publicacion']
        fecha_conclusion_publicacion = request.form['fecha_conclusion_publicacion']
      
        cursor.execute("INSERT INTO publicacion_detalle (idPublicado ,fecha_inicio_publicacion, fecha_conclusion_publicacion) VALUES (%s, %s, %s)", ( idPublicado, fecha_inicio_publicacion, fecha_conclusion_publicacion))
        conn.commit()

    return redirect(url_for('publicacion'))


@app.route('/requisicion_autorizadas')
def requisicion_autorizadas():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT  idrequisicion, folio,puesto_cubrir FROM agregar_requisicion where estado=1 ORDER BY idrequisicion')
    datos = cursor.fetchall()

    conn.close()
    return render_template("requisicion_autorizadas.html", comentarios=datos, dat='   ', datos='   ')


@app.route('/autorizadas_fdetalle/<string:idr>', methods=['GET'])
def autorizada_fdetalle(idr):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('SELECT idrequisicion, folio, puesto_cubrir FROM agregar_requisicion where estado=1 ORDER BY idrequisicion')
    datos = cursor.fetchall()

    cursor.execute('SELECT idrequisicion, folio, fecha_ela, puesto_cubrir, nombre_solicita, fecha_reclutamiento, fecha_inicio_vacante, numerodevaca, tipo_vacante FROM agregar_requisicion WHERE idrequisicion = %s', (idr,))
    dato = cursor.fetchall()

    cursor.execute('SELECT revisado, autorizado, nombre_puesto FROM autorizacion where solicitud_puesto = '+idr+' ORDER BY revisado')
    datoss = cursor.fetchall()

    return render_template("requisicion_autorizadas.html", comentarios=datos, dat=dato[0], datos=datoss[0])
   


if __name__ == "__main__":
    app.run(debug=True)
