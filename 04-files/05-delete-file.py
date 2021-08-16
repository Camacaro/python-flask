import os 

if os.path.exists('chanchito.txt'):
  os.remove('chanchito.txt')
else: 
  print('El archivo no existe')

# Borrar carpetas
# os.rmdir('myCarpeta')