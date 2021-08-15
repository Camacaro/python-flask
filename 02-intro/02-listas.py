# Las listas son como los Arrays en js
lista = [1, 2, 3]

# Copia de la lista
lista2 = lista.copy()

# Agregar datos, como un push
lista.append(4)
lista2.append(3)

# Eliminar toda la fista 
# lista.clear()

# obtener  cuantas veces se repite un valor
get_repetido = lista2.count(3)

# obtener la longitud de la lista
list_length = len(lista)

print('lista', lista)
print('lista2', lista2)
print('get_repetido lista2 de 3 es:', get_repetido)
print('longitud de la lista:', list_length)

lista_de_nombres = ['Jesus', 'Oriana', 'Alejandro', 'Mujica']

print('lista_de_nombres', lista_de_nombres)

# Acceder a los elementos de una lista
primer_nombre = lista_de_nombres[1]
print('Mi nombre:', primer_nombre)

# Eliminar el ultimo elemento de la lista
lista_de_nombres.pop()

print('Nombres', lista_de_nombres)

# Eliminar un elemento especifico
lista_de_nombres.remove('Oriana')

# cambiar el orden de array
lista_de_nombres.reverse()

print('Nombres', lista_de_nombres)

lista_de_mascota = ['torutgas', 'perros', 'aves']

# No puedo ordernar un lista que contentega string e integer
# Tienen que tener el mismo tipo de datos
# lista_de_mascota.append(4);

# En string lo ordena de A -> Z
lista_de_mascota.sort()

print('lista_de_mascota sort', lista_de_mascota)
