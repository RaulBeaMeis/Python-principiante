'''

print('Comienzo')

contador = 1
for i in [3,4,5]:
    print(f'Vuelta número: {contador}')
    print(f'Hola, ahora i vale{i} y su cuadrado es {i ** 2}')

print("Final")

'''

numero = int(input("¿De qué número quieres la tabla de multiplicar? "))
print("")

print(f'Tabla de multiplicar del número {numero}')

for i in range(1, 11):
    print(f'{i} x {numero} = {i*numero}')