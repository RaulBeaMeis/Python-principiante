class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    def frenar(self):
        return "La bicicleta está frenando"

    def avanzar(self):
        return "La bicicleta está en movimiento"

    def girar(self):
        return "La bicicleta está girando"

urbana = Bicicleta("Rojo", 8, 27.5)
hibrida = Bicicleta("Azul", 1, 29)

print("Urbana: " + str(urbana.color))
print("Comportamiento de la bicicleta urbana: " + str(urbana.girar()))
print('\n')
print("Híbrida: " + str(hibrida.cambios))
print("comportamiento de la bicicleta híbrida: " + str(hibrida.avanzar()))
