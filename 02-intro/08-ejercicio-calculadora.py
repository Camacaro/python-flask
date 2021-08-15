
# isValid = True

# primero = input('Ingrese primer nmero: ')

# try:
#   primerNumero = int(primero)
# except:
#   isValid = False

# segundo = input('Ingrese segundo nmero: ')

# try: 
#   segundoNumero = int(segundo)
# except:
#   isValid = False

# if isValid:
#   print(primerNumero + segundoNumero)
# else:
#   print('Solo se permiten numeros')


## Otro modo
# isValid = True

# primero = input('Ingrese primer nmero: ')

# try:
#   primerNumero = int(primero)
# except:
#   isValid = False

# if not isValid:
#   print('El valor ingresado no es un netero')
#   exit()

# segundo = input('Ingrese segundo nmero: ')

# try: 
#   segundoNumero = int(segundo)
# except:
#   isValid = False

# if not isValid:
#   print('El valor ingresado no es un netero')
#   exit()

# print(primerNumero + segundoNumero)

## Ejercicio con simbolo
isValid = True

primero = input('Ingrese primer nmero: ')

try:
  primerNumero = int(primero)
except:
  isValid = False

if not isValid:
  print('El valor ingresado no es un netero')
  exit()

segundo = input('Ingrese segundo nmero: ')

try: 
  segundoNumero = int(segundo)
except:
  isValid = False

if not isValid:
  print('El valor ingresado no es un netero')
  exit()

simbolo = input('Ingrese operación: ')

if simbolo == '+':
  print('Suma', primerNumero + segundoNumero)
elif simbolo == '-':
  print('Resta', primerNumero - segundoNumero)
elif simbolo == '*':
  print('Multiplicar', primerNumero * segundoNumero)
elif simbolo == '/':
  print('Multiplicar', primerNumero / segundoNumero)
else:
  print('El simbolo ingresado no es valido')