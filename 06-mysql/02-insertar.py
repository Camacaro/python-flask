import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='prueba'
)

cursor = mydb.cursor()

# script de como crear esta tabla
# cursor.execute('show create table Usuario')

sql = 'insert into Usuario (correo, usuario, edad) values (%s, %s, %s)'
values = ('micorreo@correo.co.cl', 'nombreusuario', 45)

cursor.execute(sql, values)

# Ejecutar la consulta para guardar los datos
mydb.commit()

# Verificar que se inserto
print(cursor.rowcount)
