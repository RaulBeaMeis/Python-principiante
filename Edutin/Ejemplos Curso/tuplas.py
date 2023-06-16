'''
Crear una tupla con números, luego pedir un número por teclado e indicar
cuantas veces se repite
'''

numeros = (5,6,7,8,5,5,6,90,12,14,12)

numero = int(input("Dame un número: "))

#Cuantas veces se repite el número
print("El número se repite: " + str(numeros.count(numero)) + " veces.")

#Donde se encuentra el número
print("El número " + str(numero) + " se encuentra en el indice: " + str(numeros.index(numero)))