
# parametros
# 1: nombre del archivo o la ruta
# 2: permisos del archivo, 
# 'r' (read)(defecto) | 'a' (append)(agregar cosas al archivo) 
# 'w' (writte) en caso de que este archivo no exista el va a crear uno sino lo reemplaza con lo que le digamos
# 'x' crear archivo y si existe devuelve un error
c = open('chanchito.txt')

readAllFile = c.read();

print(readAllFile)