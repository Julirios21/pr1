Tareas = [
{'Actividad': 'leer',
'TiempoT': 100,
'Realizada': 'no'},

{'Actividad': 'correr',
'TiempoT': 90,
'Realizada': 'no'},

{'Actividad': 'programar',
'TiempoT': 80,
'Realizada': 'no'},

{'Actividad': 'futbol',
'TiempoT': 120,
'Realizada': 'no'}
]

for i in Tareas:
    print(i)
cosas = input("ingrese nombre de actividad: ")
cositas = cosas.lower()
print(cositas)

for i in range(len(Tareas)):
    if cositas == Tareas[i]['Actividad']:
        print("suiiiii")
        break

    else:
        print("nouuuu")
        break