# Escribir una funcion que devuelva el volumen de una esfera por su radio
import math

def calculaVolumen(radio):
  # En vez de pow puedo usar:
  # pow(radio, 3) == radio ** 3
  volumen = (4/3) * math.pi * pow(radio, 3)
  print('El volumen es:', volumen, 'cm^3')

inputValue = input('Ingrese radio, para calcular su volumen: ')
radio = int(inputValue)
calculaVolumen(radio)
