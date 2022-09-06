# El diccionario tiene key - value

diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SARD': 'Sistema de Administración de Base de Datos'
}

print("verificar la cantidad de elementos del diccionario")
print(len(diccionario))
print(diccionario)
print()

print("Acceder a un diccionario con la llave(key)")
print(diccionario['IDE'])
print()

print("Otra forma de acceder a un elemento")
print(diccionario.get('POO'))

print("Modificar un elemento")
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

print("recorrer un elemento")
for termino in diccionario:
    print(termino)
print()

print("Acceder a la llave y el valor usando .items")
for termino, valor in diccionario.items():
    print(termino, valor)

print()
print("Otra manera de acceder a la key de un diccionario")
for termino in diccionario.keys():
    print(termino)
print()

print("Otra forma de acceder al valor de un diccionario")
for valor in diccionario.values():
    print(valor)
print()

print("Comprobar la existencia de un elemento")
print('IDE' in diccionario)  # devuelve un booleano
print()

print("Agregar un elemento")
diccionario['PK'] = 'Primary Key'
print(diccionario)
print()

print("Eliminar un elemento")
diccionario.pop('SARD')
print(diccionario)

print("vaciar un diccionario")
diccionario.clear()
print(diccionario)

print("eliminar el diccionario")
del diccionario
print()

diccionarioNuevo = {
    'Azul': 'Blue',
    'Rojo': 'Red',
    'Verde': 'Green',
    'Amarillo': 'Yellow'
}
print(diccionarioNuevo)

print()

print("eliminar un diccionario")
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

print("los diccionarios pueden almacenar distintos tipos de datos")
diccionario2 = {'Ariel':{'Edad': 40,'Altura': 1.83},'Osvaldo':[45,1.85],'Natalia':[35,1.67]}
print(diccionario2)

