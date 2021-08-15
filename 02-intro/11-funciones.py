print('========= 1er Ejercico =========')
def miFucion():
  print('Mi primera funcion')

miFucion()

print('========= 2do Ejercico =========')
def imprimeDato(argumentoUno):
  print('Mi argumento es', argumentoUno)

imprimeDato('parametro 1')

print('========= 3er Ejercico =========')
def persona(nombre, apellido):
  print('El nombre completo es', nombre, apellido)

persona('Jesus', 'Camacaro')

print('========= 4to Ejercico =========')
# nombres sera una tuplao se recibe como tupla
def personaCompleja(*nombres):
  print('Nombres ingresados ', nombres)
  print('Nombres ingresados segundo elemento ', nombres[1])

personaCompleja('Jesus', 'Alejandro', 'Oriana', 'Mujica')

print('========= 5to Ejercico =========')
def nombreCompleto(apellido, nombre):
  print(nombre, apellido)

nombreCompleto(nombre='Jesus', apellido='Camacaro')

print('========= 6to Ejercico =========')
# Con dos ** un argumento se transforma en un diccionario (objeto)
# Se le conoce como key with arguments
def namesComplete(**kwargs):
  print(kwargs['nombre'], kwargs['apellido'])

namesComplete(nombre='Jesus', apellido='Camacaro')

print('========= 7mo Ejercico =========')
def miFuncion2(argumento = 'Chanchito'):
  print('valor por defecto', argumento)

miFuncion2()
miFuncion2('Tortus')

print('========= 8vo Ejercico =========')
def miFuncionLista(lista):
  for el in lista:
    print(el)

lista = ['Chanchito', 'Feliz']
miFuncionLista(lista)

print('========= 9no Ejercico =========')
def concatenaNombres(lista):
  i = ''
  for el in lista:
    i = i + el + ' '
  return i

nombre = concatenaNombres(['Chanchito', 'Feliz'])
print(nombre)