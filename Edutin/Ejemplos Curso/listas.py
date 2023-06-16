#Introducción a los array

'''
Escribir un programa que almacene las asignaturas de un curso

asignaturas = ["Matemáticas", "Física", "Español", "Inglés"]

print(asignaturas[0])
print(type(asignaturas))

'''

#Lotería

'''
numeros = []
for i in range(6):
    numeros.append(int(input("Introducce un número")))

numeros.sort()
print(f'Los números ganadores son: {numeros}')
'''

lista = [1,4,5,6,7,8,6,"Hola"]

#Distintas funciones de los array
'''
lista.remove(6)
lista.pop(7)
del lista[0]
lista.clear()
lista.count(1)
lista.index(9)
print("Esta es la lista después de colocar el método clear:" + str(lista))
'''
lista.reverse()
print(lista)
