print("Bienvenido al conversor de monedas \n")

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:

        def dolarTo():
            if moneda_a_convertir == "1":
                print(f'{valor} dolares equivale a ${valor * 3750} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'{valor} dolares equivale a ¥{valor * 6.37} yuanes')
            elif moneda_a_convertir == "3":
                print(f'{valor} dolares equivale a €{valor * 0.76} libras esterlinas')
            else:
                print("No se reconoce la moneda a convertir")

        dolarTo()

    elif moneda_actual == 2:

        def euroTo():
            if moneda_a_convertir == "1":
                print(f'{valor} dolares equivale a ${valor * 4000} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'{valor} dolares equivale a ¥{valor * 6.93} yuanes')
            elif moneda_a_convertir == "3":
                print(f'{valor} dolares equivale a €{valor * 0.83} libras esterlinas')
            else:
                print("No se reconoce la moneda a convertir")

        euroTo()

    else:
        print("No se reconoce la moneda a convertir")

moneda_actual = int(input("Ingrese su moneda actual: \n 1. Dolar \n 2. Euro \n"))

valor = float(input("Ingrese el valor a convertir: \n"))

moneda_a_convertir = input("¿A qué moneda quiere convertirlo? \n 1. Pesos Colombianos "
                           "\n 2. Yuanes \n 3. Libras Esterlinas \n")

conversor(moneda_actual, valor, moneda_a_convertir)

'''
¿Cuánto equivale 50 dólares en pesos colombianos? - 50.0 dolares equivale a $187500.0 pesos colombianos
¿Cuánto equivale 30 euros en yuanes? - 30.0 dolares equivale a ¥207.90 yuanes
¿Cuánto equivale 15 euros en libras esterlinas? - 15.0 dolares equivale a €12.45 libras esterlinas
'''