import random

intentosRealizados= 0

print('Hola, cómo te llamas?')
nombreJugador= input()

numeroAzar= random.randint(1, 20)
print('Bueno, ' + nombreJugador + ', estoy pensando en un número entre 1 y 20.')


while intentosRealizados < 6:
   print('Intenta adivinar.') 
   estimacion = input()
   estimacion = int(estimacion)

   intentosRealizados = intentosRealizados + 1

   if estimacion < numeroAzar:
        print('Tu estimación es muy baja.') 

   if estimacion > numeroAzar:
      print('Tu estimación es muy alta.')

   if estimacion == numeroAzar:
           break


if estimacion == numeroAzar:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + nombreJugador + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

if estimacion != numeroAzar:
   numeroAzar = str(numeroAzar)
   print('Pues no. El número que estaba pensando era ' + numeroAzar)