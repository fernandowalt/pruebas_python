mi_tuple = (1, 2, 3, 4, 1)
t = (5, 5.3, 'hola', {'k': 15, 'p': 78})


print(t[3]['p'])

a, b, c, d, e = mi_tuple
print(a, b, c, d, e)
print(len(mi_tuple))
print(mi_tuple.count(1))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2))
mi_lista = list(mi_tupla)
print(mi_lista)
