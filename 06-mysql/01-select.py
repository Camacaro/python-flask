# pip3 install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='prueba'
)

cursor = mydb.cursor()

cursor.execute('select * from Usuario')

# Traer todos los datos y devolvera un lista de tuplas
# [(1, 'chanchito@faliz.com', 'fchanchito')]
allResultados = cursor.fetchall()
print(allResultados)

# traer un resultado
# (1, 'chanchito@faliz.com', 'fchanchito')
# oneResultado = cursor.fetchone()
# print(oneResultado)