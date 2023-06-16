'''
En una escuela de conducción se tiene un programa que dependiendo de la edad del usuario
debe mostrar el tipo de licencia a la que tiene derecho
Condición 1: si es menor a 16, entonces no puedes conducir
Condición 2: si es menor a 18, entonces puede obtener un permiso para conducir.
Condición 1: si es menor a 70, entonces puede obtener una licencia estandar
Condición 1: si es mayor a 16, entonces necesita una licencia especial
'''

edad = int(input("Digita tu edad: "))

if edad < 16:
    print("No tienes edad para conducir")
elif edad < 18:
    print("Puedes obtener un permiso para conducir")
elif edad < 70:
    print("Puedes obtener una licencia estándar")
else:
    print("Necesitas obtener una licencia especial")