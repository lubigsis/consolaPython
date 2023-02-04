import random
import time

#Se definen las funciones a utilizar posteriormente:

def mostrarIntroducción():
    print('Estás en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas. En una de ellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y está hambriento, y te devorará inmediatamente.')
    print()
 

def decirAdios():

    print('¡Adios!')
     
def elegirCueva():
    #Lo de abajo se llama 'validación de entrada'; se sigue ejecutando hasta que el user responda  1 o 2.
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()
    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y...')
    print()
    time.sleep(2)


#comienza a funcionar el programita:

    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('¡Te regala su tesoro!')
    else:
        print('¡Te come de un bocado!')


jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's' or jugarDeNuevo == 'SI':

    mostrarIntroducción()

    númeroDeCueva = elegirCueva()

    explorarCueva(númeroDeCueva)

    print('¿Quieres jugar de nuevo? (si o no)')

    jugarDeNuevo = input()

decirAdios()
