# Escribir una funcion que indique si un numero es par o impar

def esPar(numero):
  return numero % 2 == 0

inputValue = input('Ingrese numero: ')
numero = int(inputValue)

respuesta = esPar(numero)

if respuesta:
  print('El numero es par')
else:
  print('El numero NO es par')