
estudiantes = {
    "Juan": 5.0,
    "miguel": 4.2,
    "Luis": 4.5
}
while True:
   
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    
    try:
        calificacion = float(input("Ingrese la calificación del estudiante: "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la calificación.")
        continue

    if nombre in estudiantes:
        print(f"Actualizando la calificación de {nombre}...")
    else:
        print(f"Agregando a {nombre}...")
    estudiantes[nombre] = calificacion

print("\nLista de estudiantes y sus calificaciones:")
for nombre, calificacion in estudiantes.items():
    print(f"{nombre}: {calificacion}")
