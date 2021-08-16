# ingresar nombre y apellido e imprimirlo al reves

nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')

# In this particular example, the slice statement [::-1] 
# means start at the end of the string and end at position 0, 
# move with the step -1, negative one, which means one step backwards.

nombreCompleto = nombre + ' ' + apellido
nombreCompletoReverse = nombreCompleto[::-1]

print(nombreCompletoReverse)
