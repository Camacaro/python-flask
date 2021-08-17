# Python sin fronteras: Flask y MySQL

### 01- holamundo
Hola Mundo!
### 02- intro
Introduccion a python, variables, lista, diccionario y controles de flujo
### 03- modulos
Aprender a descargar modulos de terceros e importar modulos propios 
### 04- files
Manejar archivos del sistemas
### 05- ejercicios
Aplicar lo aprendido en introduccion con ejercicios 

### 06- mysql
Conexion a db y realizar consultas sencillas

### 07-intro-flask
Crear ambiente virtual
1. crear carpeta de proyecto
2. entrar a la carpeta y ejecutar ``` python3 -m venv venv ```
3. Activar el ambiente virtual ``` . venv/bin/activate ```
4. "(venv) jcamacaro@Notebook-G3:07-intro-flask (main)$ " con el "(venv)" me indicara que ya active mi ambiente virtual
5. Instalar flask ``` pip3 install Flask ```
6. hay que indicarle a Flask cual es el archivo que tiene que ejecutar cuando levantemos la app ``` export FLASK_APP=NAME_FILE.py ``` ``` export FLASK_APP=holamundo.py ```
7. Levantar server de flask con ``` flask run ```
8. poner el env de flask en development para que haga el reload de los cambios enlos archivos ``` export FLASK_ENV=development ```
9. salir del ambiente virtual ``` deactivate ```