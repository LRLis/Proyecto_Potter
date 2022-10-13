op = 0
while True:
    print("\nHola bienvenido \nSeleciona una opción")
    print("1)Obtener porcentaje sacado en una actividad")
    print("2)Obtener promedio de calificaciones")
    print("3)Predecir promedio sacando 50 y 100 en actividades faltantes")
    print("4)Apagar calculadora")
    op=int(input())

    if op == 1:
        print("Porcentaje obtenido en una activida")
        print("Escribe el valor de una actividad")
        
        va=float(input())
        
        print("Escribe cuanto sacaste en esa actividad")
        
        sa=float(input())
        cp=(sa*va)/100
        
        print("El porcentaje obtenido es:", cp)
    
    if op == 2:
        print("Promedio de calificaiones")
        calificaciones = int(input("Ingrese la cantidad de calificaciones: "))
        
        lista = []
        posicion = 1
        totalIngresadas = calificaciones
 
        while calificaciones > 0:
            valor = float(input("Ingrese calificación {}: ".format(posicion)))
            lista.append(valor)
            calificaciones -= 1
            posicion += 1
 
        print(lista)
 
        sumaNotas = 0
        
        for i in lista:
            
            sumaNotas = sumaNotas + i
            
        promedio = round(sumaNotas/totalIngresadas,2)
        print("El promedio de las notas ingresadas es: {}".format(promedio))

    if op == 3:
        print("Pronostico de calificaiones")
        print("Coloca cuantas calificaciones son: ")
        so=float(input())
        calificaciones = int(input("Ingrese la cantidad de calificaciones que tienes: "))
        
        lista = []
        posicion = 1
        totalIngresadas = calificaciones
        a1=(so-calificaciones)*50
        a2=(so-calificaciones)*100
        
        while calificaciones > 0:
            valor = float(input("Ingrese calificación {}: ".format(posicion)))
            lista.append(valor)
            calificaciones -= 1
            posicion += 1
 
        print(lista)
 
        sumaNotas = 0
        
        for i in lista:
            
            sumaNotas = sumaNotas + i
            
        promedio1 = round((sumaNotas+a1)/so,2)
        promedio2 = round((sumaNotas+a2)/so,2)
        
        print("El promedio sacando 50 en las calificaciones faltantes: {}".format(promedio1))
        print("El promedio sacando 100 en las calificaiones faltantes: {}".format(promedio2))

    if op == 4:
        break
    
    if op > 4:
        print("No existe esta opción")
    
