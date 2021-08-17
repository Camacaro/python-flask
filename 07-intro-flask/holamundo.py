from flask import Flask, request, url_for, redirect, abort, render_template

# __name__ es el nombre del archivo en este caso es holamundo
app = Flask(__name__)

# curl -X GET http://localhost:5000
@app.route('/')
def index():
  return 'hola mundo'

# Por defecto es GET
# GET, POST, DELETE
# PUT(actualizar un recurso completo), 
# PATCH(actualizar parcialmente un recurso)
# Forzar para que sea un entero <int:post_id>
# curl -X GET http://localhost:5000/post/1
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
  if request.method == 'GET':
    return 'El id del post es: ' + post_id
  else:
    return 'Este es otro metodo y no GET '

# @app.route('/post/<post_id>', methods=['POST'])
# def savePost(post_id):
#   return 'El id del post es: ' + post_id

@app.route('/user/<user>')
def user(user):
  return 'Usuario ingresado: ' + user

# curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000 
@app.route('/test', methods=['POST'])
def test():
  # Formar URLs url_for
  nombreFuncion = 'index'
  print('== url_for', url_for(nombreFuncion))
  nombreFuncion2 = 'post'
  print('== url_for', url_for(nombreFuncion2, post_id=2))
  print('== form', request.form)
  print('== form', request.form['llave1'])
  print('== form', request.form['llave2'])
  return 'Test'

# curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/test-redirect
@app.route('/test-redirect', methods=['POST', 'GET'])
def testRedirect():
  nombreFuncion = 'post'
  path = url_for(nombreFuncion, post_id=2)
  return redirect(path)

# Abortar peticioón
@app.route('/test-abort', methods=['POST', 'GET'])
def testAbort():
  # abort(401)
  abort(403)
  nombreFuncion = 'post'
  path = url_for(nombreFuncion, post_id=2)
  return redirect(path)


# Redireccionar Templates HTML
# Flask buscara una carpeta llamada templates
@app.route('/test-template', methods=['GET'])
def testTemplate():
  return render_template('template.html')

# Retornar JSON (Diccionario)
@app.route('/test-json')
def testJson():
  return {
    "username": "Jesus Camacaro",
    "email": "root@mail.com"
  }

# Extencion
# Redireccionar Templates HTML
# Flask buscara una carpeta llamada templates
@app.route('/home', methods=['GET'])
def home():
  return render_template('home.html', mensaje='Hola Mundo')