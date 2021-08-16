# Escribir una funcion que indique cuantas vocales tiene una palabra

def searchCountWord(word, vocal):
  return word.count(vocal)

palabra = input('Ingrese palabra: ')
vocal = input('Ingrese vocal: ')

repetidoCantidad = searchCountWord(palabra, vocal)

print('La cantidad de veces repetida la vocal', vocal, 'es', repetidoCantidad)

print('===== Respuesta Curso ====')
# ENtendi mal el ejercicio, tengo que buscar son las vocales que hay en la palabra
vocales = 0
for x in palabra:
  y = x.lower()
  vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print('Vocales', vocales)