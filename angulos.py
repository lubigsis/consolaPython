#Diseñe un algoritmo para convertir grados sexagesimales (S) a grados centesimales 
# (C) y radianes (R).
#  Considere las siguientes fórmulas:
# C= 200x S/ 180
# R= 3.1416xS/180

print('Ingrese el valor del ángulo')
S = input()
S = float(S)


C = 200 *  S/ 180
R = 3.1416 * S/180

print(f'El resultado en centesimal es {C}')

print()

print(f'El resultado en radianes es {R}')
