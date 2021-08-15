print('========= 1er Ejercico =========')
usuarios = ['Chanchitp feliz', 'felipe', 'roberto', 'nicolas']
for usuario in usuarios:
  print(usuario)


print('========= 2do Ejercico =========')
usuario = 'Canchito Feliz'
# Deletrear
for c in usuario:
  print(c)

print('========= 3ro Ejercico =========')
for usuario in usuarios:
  if usuario == 'roberto':
    break
  print(usuario)

print('========= 4to Ejercico =========')

for usuario in usuarios:
  if usuario == 'roberto':
    continue
  print(usuario)

print('========= 5to Ejercico =========')

for usuario in usuarios:
  if usuario == 'roberto':
    continue
  print(usuario)

print('========= 6to Ejercico =========')
for x in range(3, 6):
  print(x)

print('========= 7to Ejercico =========')
for x in range(3, 27, 3):
  print(x)
else: 
  print('Hemos terminado')
print('Fuera del for')

print('========= 8vo Ejercico =========')
edades = [24, 25, 26, 35]

for usuario in usuarios:
  print('---')
  for edad in edades:
    print('Usuario', usuario, 'con la edad', edad)