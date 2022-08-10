from pydoc import cli


diccionario = {'walter': 'hombre', 'maria': 'mujer'}

print(type(diccionario))
print(diccionario['maria'])


cliente = {'nombre': 'jual', 'apellido': 'fuentes', 'perso': 88, 'talla': 1.76}

consulta = (cliente['apellido'])

print(consulta)


dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}

print(dic['c3']['s1'])

dicc = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}

print(dicc['c2'][1].upper())

nuevo_diccionario = {1: 'a', 2: 'b'}
nuevo_diccionario[3] = 'c'
nuevo_diccionario[2] = 'B'
print(nuevo_diccionario)
print(nuevo_diccionario.keys())
print(nuevo_diccionario.values())
print(nuevo_diccionario.items())

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])
