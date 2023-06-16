'''
Primer ejemplo:
Crear un programa que reciba el número de años que tiene nuestro ordenador.
Imprimir en consola si es nuevo o viejo.
Condiciones: Si es menor o igual a 2, entonces es nuevo.
Pero, si es mayor a 2 años, entonces es viejo.
'''

antiguedad = int(input("¿Cuantos años tiene tu ordenador?"))

if antiguedad >= 0 and antiguedad <=2:
    print("Tu ordenador es nuevo")
else:
    print("Tu ordenador es viejo")