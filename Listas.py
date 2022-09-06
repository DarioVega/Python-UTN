# La lista mantiene un orden y se puede modificar

nombres = ['Natalia', 'Osvaldo', 'Liliana', 'Ariel']
print(nombres)
print()

print("Muestra el rango seleccionado sin incluir el índice 2:")
print(nombres[0:2])
print()

print("ir desde el inicio de la lista al índice (sin incluirlo):")
print(nombres[:3])
print()

print("ir desde el índice indicado hasta el final:")
print(nombres[1:])
print()

print("Modificamos un valor:")
nombres[3] = 'Alberto'
print(nombres)
print()

print("Iterar una ista:")
for nombre in nombres:
    print(nombre)
else:
    print("se acabaron los elementos de la lista")
print()

print("preguntarnos cuantos elementos tiene")
print(len(nombres))
print()

print("agregamos un elemento")
nombres.append("Marcelo")
print(nombres)
print()

print("insertar un elemento en un índice específico")
nombres.insert(2, "Mariano")
print(nombres)
print()

print("eliminamos un elemento de la lista")
nombres.remove("Mariano")
print(nombres)
print()

print("eliminamos el último elemento de la lista")
nombres.pop()
print(nombres)
print()

print("eliminamos un índice específico")
del nombres[2]
print(nombres)
print()

print("vaciar la lista")
nombres.clear()
print(nombres)
print()

print("eliminar la lista")
del nombres
print()

print("concatenacion de listas")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)
print()

print("extender una lista")
lista3.extend([7, 8, 9, 1])
print(lista3)
print()

print("función para ubicar un elemento en una lista")
print(lista3.index(5))
print()

print("Saber cuantos elementos hay repetidos")
print(lista3.count(1)) #cuenta cuantos valores iguales hay
print()

print("poner una lista al reves")
lista3.reverse()
print(lista3)
print()

print("multiplicar una lista usando sus elementos")
lista3 = lista3 * 2 #se duplica
print(lista3)
print()

print("Metodos de ordenamiento")
lista3.sort()
print(lista3)
print()

print("ordenar descendentemente")
lista3.sort(reverse=True)
print(lista3)
print()

print("Pilas")
pila = [1, 2, 3]
print()
print("Agregamos elementos a la pila")
pila.append(4)
pila.append(5)
print(pila)
print("sacamos elementos desde el final con pop()")
elementoBorrado = pila.pop()
print("quita el último elemento y lo guarda en la variable")
print(f"sacamos el elemento {elementoBorrado}")
print(f"la pila ahora queda así: {pila}")
print()

print("Colas (FIFO)")
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
print(cola)
print("agregamos elementos")
cola.append('Natalia')
cola.append('José')
print(cola)
print("quitamos elementos")
seRetira = cola.pop(0)
print(f'atendido el cliente: {seRetira}')
print(cola)
