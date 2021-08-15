# La diferencia de tuplas con lista es que estas no son mutables
# No se puede modificar
tupla = ('hola', 'mundo', 'somos', 'tupla')

index_somos = tupla.index('somos')

print(tupla)
print('count', tupla.count('hola'))
print('index', tupla.index('mundo'))
print('acceso por indice:', tupla[index_somos])

# Pasar una tupla a lista
lista_de_tupla = list(tupla);
lista_de_tupla.append('lista')
print('lista_de_tupla', lista_de_tupla)