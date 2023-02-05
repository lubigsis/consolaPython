
import random
import time

#declaro funciones:

def mostrarIntroduccion():
    print()
    print('Elige qué operación quieres intentar. Tienes 10 intentos')
    time.sleep(2)
    print()
    print()
    print('Si quieres hacer sumas, escribe: sumar')
    time.sleep(2)
    print('Si quieres hacer restas, escribe: restar')
    time.sleep(2)
    print('Si quieres hacer multiplicaciones, escribe: multiplicar')
    time.sleep(2)
    print('Si quieres hacer divisiones, escribe: dividir')
    time.sleep(2)
    print()
    print('Si quieres dejarlo para otro día, escribe: salir')
    print()


def despedida():
    print('¡Hasta pronto!')


#-------------------------------------------------defino las 4 operaciones-----------
def suma():
 num1= random.randint(11, 99)
 num2= random.randint(11, 99)

 resultadoSuma= num1 + num2 

 num1 = str(num1)
 num2 = str(num2)

 print(num1)
 print()
 print('+')
 print()
 print(num2)
 print()


def resta():
  num1= random.randint(11, 99)
  num2= random.randint(11, 99)

  resultadoResta= num1 - num2 

  num1 = str(num1)
  num2 = str(num2)

  print(num1)
  print()
  print('-')
  print()
  print(num2)
  print()

def multiplicacion():
  num1= random.randint(11, 99)
  num2= random.randint(11, 99)

  resultadoMultiplicacion= num1 * num2 

  num1 = str(num1)
  num2 = str(num2)

  print(num1)
  print()
  print('*')
  print()
  print(num2)
  print()

def division():
  num1= random.randint(11, 99)
  num2= random.randint(2, 10)

  resultadoDivision= num1 // num2 

  num1 = str(num1)
  num2 = str(num2)

  print(num1)
  print()
  print('/')
  print()
  print(num2)
  print()


#---------------------------------------------------Inicia el programa-------------------

mostrarIntroduccion()

operacionElegida= input()
counter= 0

if operacionElegida == 'sumar' or operacionElegida == 'SUMAR':
    while counter < 10:
      suma()      
      estimacionUser= input()
      counter= counter +1 
   

elif operacionElegida == 'restar' or operacionElegida == 'RESTAR':
      while counter < 10:
        resta()
        estimacionUser= input()
        counter= counter +1

elif operacionElegida == 'multiplicar' or operacionElegida == 'MULTIPLICAR':
      while counter < 10:
        multiplicacion()
        estimacionUser= input()
        counter= counter +1

elif operacionElegida == 'dividir' or operacionElegida == 'DIVIDIR':
      while counter <10:
        division()
        estimacionUser= input()
        counter= counter +1

else:
     print('Escribe corectamente la operación que deseas realizar')




