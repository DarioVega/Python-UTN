# Operaciones de conjuntos con listas
# Escriba un programa que tenga  2 listas y que a continuación
# cree las siguientes listas ( no debe haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

primeraLista = ['Alberto', 'Mariela', 'Ariel', 'Facundo', 'Manuel', 'Mario']
segundaLista = ['Eugenia', 'Alberto', 'María', 'Mariela', 'Agustina', 'Silvia']

primeraLista = set(primeraLista)
segundaLista = set(segundaLista)

union = list(primeraLista | segundaLista)
soloPrimera = list(primeraLista - segundaLista)
soloSegunda = list(segundaLista - primeraLista)
interseccion = list(primeraLista & segundaLista)

print(f"1 Lista de palabras que aparecen en las listas: \n{union}")
print()
print(f"2 Lista de palabras que aparecen en la primera lista, pero no en la segunda: \n{soloPrimera}")
print()
print(f"3 Lista de palabras que aparecen en la segunda lista pero no en la primera: \n{soloSegunda}")
print()
print(f"4 Lista de palabras que aparecen en ambas listas (coincidencia): \n{interseccion}")

