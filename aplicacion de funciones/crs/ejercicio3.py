
calificaciones = {
    "juan": 85,
    "miguel": 92,
    "Luis": 78
}

nombre_max = max(calificaciones, key=calificaciones.get)

print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
