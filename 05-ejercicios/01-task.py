
# Multipliclar dos numeros sin usar el simbolo de multiplicar 

input1 = input('Ingrese el primer valor: ')
input2 = input('Ingrese el segundo valor: ')

valor1 = int(input1)
valor2 = int(input2)

resultado = 0
# range(0, valor2)
for i in range(valor2):
  resultado += valor1

print('El resultado es:', resultado)