#Estás haciendo un sistema de tickets. El precio de cada ticket es $100.
#Los niños menores de 3 años no pagan.
#Tu programa tiene que tomar la edad de 5 personas en un input, y en un output mostrar el precio total 
#de los tickets.
print("Escribe tu edad")
edad= int(input())
ticket= 0
personaContador= 0

if edad >3:
    while personaContador <5:
        ticket= ticket + 100
        personaContador+=1
        print(ticket)
else:
    print('Los menores de 3 años no abonan')

    


