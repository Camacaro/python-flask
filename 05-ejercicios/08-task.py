# Escribir una aplicacion que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la duma de los numeros ingresados

lista = []

while True:
  print('Ingrese numeros y para salir escriba "basta"')
  valor = input('Ingrese valor: ')
  if valor == 'basta':
    break
  else:
    try:
      valor = int(valor)
      lista.append(valor)
    except:
      print('Dato invalido')
      exit()

resultado = 0
for x in lista:
  resultado += x

print('Suma total', resultado)