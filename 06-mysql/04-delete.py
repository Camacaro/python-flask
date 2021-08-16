import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='prueba'
)

cursor = mydb.cursor()

sql = 'delete from Usuario where id = %s'
values = (2, )

cursor.execute(sql, values)

# Ejecutar la consulta para eliminar
mydb.commit()

