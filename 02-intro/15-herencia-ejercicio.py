
class Animal:
  def __init__(self, nombre, onomatopeya):
    self.nombre = nombre
    self.onomatopeya = onomatopeya

  def saludo(self):
    print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
  tipo = 'gato'
  # Al crear mi init va a ignorar al del padre
  def __init__(self, nombre, onomatopeya):
    # como va a ignorar al padre tengo que llamar a la clase padre y pasarle 
    # sus argumentos
    Animal.__init__(self, nombre, onomatopeya)
    print('Hola, soy un gato extendido')

class Perro(Animal):
  tipo = 'perro'
  # Extender el comportamiento que tiene el metodo init del padre
  # al hacer init reemplazo el init del padre y tengo que llamar al init
  # del padre para mantener el comportamiento del padre
  def __init__(self, nombre, onomatopeya):
    super().__init__(nombre, onomatopeya)
    print('instanciando un perro')

class Canario(Animal):
  tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Joy', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()