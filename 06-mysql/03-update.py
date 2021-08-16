import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='prueba'
)

cursor = mydb.cursor()

sql = 'update Usuario set correo = %s where id = %s'
values = ('micorreo@correo.com', 2)

cursor.execute(sql, values)

# Ejecutar la consulta para guardar los datos
mydb.commit()

