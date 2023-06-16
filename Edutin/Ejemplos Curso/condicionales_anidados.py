password = input("Ingresa la contraseña: ")

if (len(password) >= 8):
    print("Muy bien, contraseña suficientemente larga")

    if (password == 'Prueba12345'):
        print("Además, es la correcta")
    else:
        print("Pero es incorrecta")

else:
    print("Tu contraseña es muy correcta e insegura")