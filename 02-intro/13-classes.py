
# nombre = "Felipe"
# apellido = 'Rodriguez'

class Usuario:
  # Esto es como el constructor
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  # El nombre de self podria ser otro nombre
  # pero por convencion se llama self
  def saludo(self):
    print('Hola, mi nombre es', self.nombre, self.apellido)
    

usuario = Usuario('Felipe', 'Rodrifuez')
usuario2 = Usuario('Juan', 'Perez')

print(
  usuario.nombre,
  usuario.apellido
)

print(
  usuario2.nombre,
  usuario2.apellido
)

usuario.saludo()
usuario2.saludo()

usuario.apellido = "Nuevo apellido"
usuario.saludo()

# Eliminar propiedades
# del usuario.nombre
# usuario.saludo()

# Eliminar objeto completo
# del usuario
# print(usuario)