print("=================================================================")

print("Escribe las calificaciones usando escala de 0 a 100")
print("Calificaión obtenida por porcentaje de valor")
print("Escribe el valor de una actividad")
va=float(input())
print("Escribe cuanto sacaste en esa actividad")
sa=float(input())

cp=(sa*va)/100

print("El porcentaje obtenido es:", cp)


print("=================================================================")

print("Promedio de calificaiones")
print("Se detiene al colocar un número negativo, y no se toma en cuenta para el promedio")
n=0
c=0
sum=0
while n>=0:
    n=float(input("Pon un número: "))
    if n>0:
        c=c+1
        sum=sum+n
print("Total de números ingresados: ", c)
print("Promedio: ",sum/c)

print("=================================================================")

print("Pronostico de calificaiones")
print("Coloca cuantas calificaciones son: ")
so=float(input())
print("Calificaciones que tienes: ")
ob=float(input())

a=so-ob

print("Coloca las calificaiones que tienes: ")
print("Se detiene al colocar un número negativo, y no se toma en cuenta para el promedio")

n=0
c=0
sum=0
while n>=0:
    n=float(input("Pon un número: "))
    if n>0:
        c=c+1
        sum=sum+n

print("Total de números ingresados: ", c)
print("Promedio de las calificaiones sacando 50 en actividades restantes: ",(sum+a*50)/so)
print("Promedio de las calificaiones sacando 100 en actividades restantes: ",(sum+a*100)/so)

print("=================================================================")
