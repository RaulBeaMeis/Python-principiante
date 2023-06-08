#Concatenación de strings en la misma variable#
mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

print("Concatenación:")

#Concatenación entre distintos strings de distintas variables#
mensaje = "Hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)

#Concatenación de strings y un número convirtiendo el número a string#
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
print("El resultado de la suma es: " + str(resultado))

#Buscar la posición de una subcadena#
print("Busqueda:")

mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)

#Extracción de un string#

print("Extracción:")

mensaje = "Hola Ernesto"
extraer_cadena = mensaje[1:8]
print(extraer_cadena)

#Comparación de strings#


print ("Comparación:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
