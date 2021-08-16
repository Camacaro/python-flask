# Escribit una funcion que reciba nombre y apellido y los vaya agregando a un archivo
import os 

nameFile = '09-task.txt'

def createFile(name):
  c = open(nameFile, 'w')
  c.write('\n' + ' ' + name)
  c.close()

def addName(name):
  c = open(nameFile, 'a')
  c.write('\n' + ' ' + name)
  c.close()

def execute(name):
  if os.path.exists(nameFile):
    addName(name)
  else: 
    createFile(name)

nameComplete = input('Ingrese nombre y apellido: ')
execute(nameComplete)