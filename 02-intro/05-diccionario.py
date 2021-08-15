# Un diccionario es un objecto como en JS
diccionario = {
  "nombre": "Jesus",
  "apellido": "Camacaro",
  "edad": 25
}

print(diccionario)
print(diccionario["nombre"])
print(diccionario.get('nombre'))

diccionario["nombre"] = "Alejandro"

print(diccionario)

cantidad_de_elementos = len(diccionario)

print('cantidad_de_elementos', cantidad_de_elementos)

# Agregar propiedades
diccionario['ronronea'] = "Sí"

print(diccionario)

# Clonar diccionario
# copia_persona = diccionario.copy()
# Clonar diccionario con la palabra reservada dict
copia_persona = dict(diccionario)

# Borrar propiedades
diccionario.pop('ronronea')
# Borrar la ultima propiedad del item
diccionario.popitem();
# Borrar con la palabra reservada del
del diccionario['apellido']

print(diccionario)

print('copia persona', copia_persona)

# Borrar todo el diccionario
copia_persona.clear()

print('copia persona', copia_persona)

fluffy = {
  'nombre': "Fluffy",
  'edad': 4
}

# Diccionario anidados
gatitos = {
  "Fluffy": fluffy,
  'Mamba': {
    'nombre': 'Black Mamba',
    'edad': 12
  }
}

print('Gatitos', gatitos)

# Otra forma de crear diccionario
perritos = dict(nombre="Chanchito Feliz", edad=6)
print('pettiros', perritos)