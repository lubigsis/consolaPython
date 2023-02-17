print("La magia sí existe, le dijo muy emocionada Camila a su abuelita...")
print()
print('¿Cómo quieres continuar? ¡Anímate a elegir una opción y deja tu imaginación volar!')
print()

print('Opción 1)... \nOpción 2)... \nOpción 3)...')

respuestaUser= input()

historias = [
    "0- Acá escribir la primera historia0. \n Elige otra opción para continuar: ",
    "1- Acá escribir la segunda historia1. \n Elige otra opción para continuar: ",
    "2- Acá escribir la segunda historia2. \n Elige otra opción para continuar: "
]

def mostrarHistoria(numeroOpcion):
    text = historias[numeroOpcion]
    print(text)

    respuesta = input()
    mostrarHistoria(int(respuesta))

    mostrarHistoria(0)

    #terminar