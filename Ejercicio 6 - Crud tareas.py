Tareas = [
{'Actividad': 'Leer',
'TiempoT': 100,
'Realizada': 'no'},

{'Actividad': 'Correr',
'TiempoT': 90,
'Realizada': 'no'},

{'Actividad': 'Programar',
'TiempoT': 80,
'Realizada': 'no'},

{'Actividad': 'Futbol',
'TiempoT': 120,
'Realizada': 'no'}
]
print("---------------------------------------------")
tiempoP = int(input("ingrese tiempo disponible en minutos: "))
mainloop = True
while mainloop:     
    print("--------------------------------------------------")
    print("Menú")
    print("1 - Crear nueva tarea")
    print("2 - Leer Tareas")
    print("3 - Eliminar Tareas")
    print("4 - Realizar tarea")
    print("5 - Añadir tiempo")
    print("6 - Salir")
    op = int(input("Ingrese una opción: ") )

    if op == 1:
        for i in Tareas:
            print(i)
        Actividad = input("ingrese nombre de la actividad: ")

        TiempoT = int(input("ingrese Tiempo que demora: "))
        Realizada = 'no'

        Tarea = {'Actividad': Actividad, 'TiempoT': TiempoT , 'Realizada': Realizada,}
        Tareas.append(Tarea)

    if op == 2:
        for i in Tareas:
            print(i)

    if op == 3:
        for i in Tareas:
            print(i)
        TareaElim = input("Elija la actividad a eliminar: ")
        for i in range(len(Tareas)):            
            if TareaElim == Tareas[i]['Actividad']:
                Tareas.pop(i)
                print(f"Tarea -{TareaElim}- eliminada con exito")
                break

    if op == 4:
        for i in Tareas:
            print(i)
        TareaElim = input("Elija la actividad a realizar: ")
        for i in range(len(Tareas)):            
            if TareaElim == Tareas[i]['Actividad']:
                if Tareas[i]['TiempoT']<= tiempoP:  
                    Tareas[i]['Realizada'] = 'si'
                    tiempoP = tiempoP - Tareas[i]['TiempoT'] 
                    Tareas.pop(i)
                    print("La tarea se realizo con exito")
                    break
                else:
                    print(f"A usted le quedan {tiempoP}minutos, requiere de mas minutos")
            
    if op == 5:
        print(f"A usted le queda {tiempoP}minutos")
        tiempoP = tiempoP + int(input("ingrese el tiempo a añadir: "))

    if op == 6:
        mainloop = False

    
    print("--------")
    print(f"le quedan {tiempoP} minutos")