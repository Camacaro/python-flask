# Escribir una funcion que indique si el usuario es mayor de edad

def esMayorDeEdad(edad):
  if edad >= 18:
    print('Es mayor de edad')
  else:
    print('No es mayor de edad')

inputValue = input('Ingrese su edad: ')
edad = int(inputValue)
esMayorDeEdad(edad)


print('===== Respuesta Curso ====')
def esMayor(usuario):
  return usuario.edad > 17

class Usuario:
  def __init__(self, edad):
    self.edad = edad

usuario = Usuario(edad)
resultado = esMayor(usuario)
print(resultado)