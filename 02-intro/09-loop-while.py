
i = 0

while i < 6:
  print('loop', i)
  if i == 5:
    print('break....')
    break
  
  if i == 4:
    print('continuar... vuelve al while')
    i += 1
    continue
  
  i += 1
print('loop terminado')

print('######################################')

k = 0
while k < 5:
  k += 1
  if k == 3:
    print('continue')
    continue
  print('loop', k)