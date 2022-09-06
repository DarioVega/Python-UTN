# El set no tiene un orden, no se puede modificar y no permite elementos repetidos
# El set no tiene índice

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
print(len(planetas))
print()

print("Revisar si un elemento existe en el set")
print('Marte' in planetas)
print()

print("Agregar un elemento")
planetas.add('Tierra')
print(planetas)
print()

print("Eliminar elementos, puede arrojar un error si el elemento no existe")
planetas.remove('Júpiter')  # si escribo mal da error
planetas.discard("Tierra")  # si escribo mal no ejecuta pero tampoco tira error
print(planetas)
print()

print("vaciar el set")
planetas.clear()
print(planetas)
print()

print("eliminar el set")
del planetas
print()

print("para inicializar un conjunto vacío tengo que hacerlo con set()"
      "ya que si lo hago con {} no me deja usar el .add")
conjuntovacio1 = {}
conjuntovacio2 = set()
conjuntovacio2.add(79)
conjuntovacio2.add(5)
print(conjuntovacio2)
print(3 not in conjuntovacio2)
print()

print(conjuntovacio1 == conjuntovacio2)

print("operaciones de conjuntos")
print("concatenación de conjuntos")
conjunto1 = {"bye","hola","adios"}
conjunto2 = {"bye","Hola","adios"}
conjunto3 = conjunto1 | conjunto2
print(conjunto3)
print()

print("conjunción, trae los elementos en común")
conjunto3 = conjunto1 & conjunto2
print(conjunto3)
print()

print("mostrar los elementos del conjunto2 que no estén en el conjunto1")
conjunto3 = conjunto2 - conjunto1
print(conjunto3)
print()

print("averiguar si un conjunto es subconjunto de otro")
conjunto3 = conjunto1 | conjunto2 # concatenamos los dos conjuntos
print(conjunto1.issubset(conjunto3)) # preguntamos si es subconjunto
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))
print()

print("averiguar si es un superconjunto, si incluye a otro")
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))
print()

print("averiguar si son disconexos, no comparten ningún elemento")
print(conjunto1.isdisjoint(conjunto2))
print()

print("convertir un conjunto en inmutable, no se puede agregar, modificar ni eliminar elementos")
conjunto1 = frozenset



