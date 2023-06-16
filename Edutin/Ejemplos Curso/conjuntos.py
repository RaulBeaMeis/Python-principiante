'''
add // Añade un elemento al final del conjunto
clear // Elimina toda la información del conjunto
pop // Devuelve y elimina un elemento arbitrario o devuelve un error si está vacío
remove // Intenta eliminar un elemento del conjunto, si no existe eleva un error
union // Devuelve un conjunto con todos los elementos de ambos conjuntos
'''

#1 forma de crear conjuntos
alumnos = {"Andrea", "Ruby", "Marcos", "Marlon", "Jose"}

#print(alumnos)

#2 forma de crear conjuntos
lenguajes = set(["PHP", "Java", "C", "Python"])
print(lenguajes)

#lenguajes.add("C#")
#lenguajes.clear()
#lenguajes.pop()
#lenguajes.remove("Java")

todos = alumnos.union()

print(todos)