# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b
if 2 < 5:
  print('2 es menor que 5')

if 2 == 3:
  print('2 es igual a 3')
else:
  print('2 NO es igual a 3')

if 2 > 5:
  print('2 es mayor que 5')
elif 2 < 5:
  print('2 es menor que 5 elif')

if 2 > 5:
  print('2 es mayor que 5')
elif 2 > 6:
  print('2 es mayor que 6')
else:
  print('2 es meno else')

# ir corto
if 2 < 5: print('if en una linea')
# ternario
print('Cuando devuelve TRUE') if 5 > 2 else print('Cuando devuelve FALSE')

ternario = 'positivo' if 5 > 2 else 'negativo'
print('ternario', ternario)

if 2 < 4 and 3 > 2:
  print('Ambas son positivas')

if 2 < 5 and 3 < 2:
  print('Hay una falsa, esto no se mostrara')

if 1 < 0 or 1 > 0:
  print('Una de las dos condiciones devolvio TRUE')