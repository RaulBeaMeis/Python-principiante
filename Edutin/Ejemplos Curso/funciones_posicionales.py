def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

resultado = suma(10,10,10)

print(resultado)

def lenguaje(nombre, **kwargs):
    print(f'Hola {nombre}')
    print("Buscando información acerca de tus lenguajes favoritos...")
    print("Cargando información... \n")

    print("Información: ")
    contador = 0
    for clave in kwargs:
        contador += 1
        print(f'Tu {contador} lenguaje favorito es: {kwargs[clave]}')

lenguaje("Eduardo", lenguaje1 = "Ruby", lenguaje2 = "Python", lenguaje3 = "Java", lenguaje4 = "PHP")