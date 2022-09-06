# Eliminar los duplicados de una lista
# Escribe un programa donde haya una lista y que a continuación
# se eliminen los elementos repetidos. Por último mostrar la lista

lista = [1, 2, 3, 'Ariel', 7, 7, 3, 'Alberto', 5, 'Ariel']
#conjunto = set(lista) #convertimos la lista en un set
#lista = list(conjunto)
lista = list(set(lista))
print(lista)
