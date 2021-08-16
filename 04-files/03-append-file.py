

c = open('chanchito.txt', 'a')

c.write('\nagregamos una nueva linea a nuestro archivo')

c.close()

x = open('chanchito.txt')

print(x.read())