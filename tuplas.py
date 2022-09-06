# La tupla mantiene un orden y no se puede modificar

cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))
print()

print("acceder a un elemento")
print(cocina[0])
print()

print("mostrar de manera inversa")
print(cocina[-1])
print()

print("acceder a un rango")
print(cocina[0:1])
print()

print("Ejemplo de tupla")
verduras = ('papa',) #una tupla necesita de la coma sino sería un string
print()

print("recorremos los elementos de la tupla")
for cocinar in cocina:
    print(cocinar, end=' ')
print()

#Conversion de tupla a lista (no aconsejado)
cocinaLista = list(cocina)
cocinaLista[0]='plato'
cocina = tuple(cocinaLista)
print('\n', cocina)
print()

print("eliminar una tupla")
del cocina
print()

tupla = (4, "hola", 6.78, [1, 2, 78], 4, "hola")
print(tupla)
print()
print("averiguar si un elemento está dentro de una tupla")
print(4 in tupla)
