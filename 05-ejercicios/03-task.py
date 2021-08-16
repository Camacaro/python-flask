# Escribir una funcion que encuentre el elemento menor de una lista

lista = [3, 2, 5, 9, 7, 1, 6, 5, 2, -24, -16, -14]

menorValor = lista[0]

for el in lista:
  if(menorValor > el):
    menorValor = el

print('EL valor menor es:', menorValor)

print('===== Respuesta Curso ====')
menor = 'init'

for x in lista:
  if menor == 'init':
    menor = x
  else:
    menor = x if x < menor else menor

print('EL valor menor es:', menor)  