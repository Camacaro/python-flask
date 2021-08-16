# https://pypi.org/project/camelcase/
# pip install camelcase
from camelcase import CamelCase

# If you have particular words that you want to skip then you can do the following...
# CamelCase('little', 'another')

c = CamelCase()
s = 'esta oracion necesita CamelCase'

value = c.hump(s)

print(value)