#Introducción a diccionarios python
'''
#Primera forma de crear un diccionario

diccionario = {
    "Nombre": "Sara",
    "Edad": 28,
    "Documento": 456234
}

print(diccionario)

#Segunda forma de crear un diccionario

diccionario_segunda_forma = dict(Nombre='Paola',
                                 Edad=37,
                                 Documento=2394534)

print(diccionario_segunda_forma)

#Tercera forma de crear un diccionario

diccionario_tercera_forma = dict([
    ('Nombre', 'Jose'),
    ('Edad', 37),
    ('Documento', 232345)
])

print(diccionario_tercera_forma)

'''


inventario = {"Manzana": 235, "Peras": 400, "Naranjas": 250, "Sandias": 500}

#inventario.keys()
#inventario.values()

print(inventario.items())