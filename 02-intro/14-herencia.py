
class Usuario:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def saludo(self):
    print('Hola, mi nombre es', self.nombre, self.apellido)

# Herencia
class Admin(Usuario):
  def superSaludo(self):
    print('Hola, me llamo,', self.nombre, ' y soy administrador')

userAdmin = Admin('Jesus', 'Camacaro')

userAdmin.saludo()
userAdmin.superSaludo()