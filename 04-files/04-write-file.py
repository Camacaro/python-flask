
c = open('chanchito.txt', 'w')

c.write('\nSolo este texto estara')

c.close()

x = open('chanchito.txt')

print(x.read())