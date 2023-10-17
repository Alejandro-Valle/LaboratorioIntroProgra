# Se definen estas dos variables que sirven despues para poner un límite en los ciclos.
num_lineas_produccion = 2
max_empleados_por_linea = 20

# se crea una lista para almacenar las lineas de producción
lineas_produccion = []

# Ciclo para cada línea de producción
for i in range(num_lineas_produccion):
    print(f"Línea {i + 1}:")
    
    metros_vendidos = float(input(f"Metros vendidos en línea {i + 1}: "))
    precio_por_mt2 = float(input(f"Precio por metro cuadrado en línea {i + 1}: "))
    
    empleados = []
    total_costo_empleados = 0
    
    # Bucle para capturar información de empleados
    while len(empleados) < max_empleados_por_linea:
        horas_trabajadas = float(input(f"Horas trabajadas por empleado {len(empleados) + 1} (0 para finalizar): "))
        if horas_trabajadas == 0:
            break
        costo_hora = float(input(f"Costo por hora del empleado {len(empleados) + 1}: "))
        empleado = {"horas_trabajadas": horas_trabajadas, "costo_hora": costo_hora}
        empleados.append(empleado)
        total_costo_empleados += horas_trabajadas * costo_hora
    
    # Cálculo de la ganancia neta
    ganancia_total = metros_vendidos * precio_por_mt2
    ganancia_neta = ganancia_total - total_costo_empleados
    
    # Cálculo del índice de eficiencia
    num_empleados = len(empleados)
    indice_eficiencia = ganancia_neta / num_empleados
    
    # Almacenar información en la lista de líneas de producción
    linea = {
        "metros_vendidos": metros_vendidos,
        "precio_por_mt2": precio_por_mt2,
        "empleados": empleados,
        "ganancia_neta": ganancia_neta,
        "indice_eficiencia": indice_eficiencia
    }
    lineas_produccion.append(linea)

# Encontrar la línea con el mayor índice de eficiencia
max_indice_eficiencia = 0
linea_mayor_eficiencia = 0

for i, linea in enumerate(lineas_produccion):
    if linea["indice_eficiencia"] > max_indice_eficiencia:
        max_indice_eficiencia = linea["indice_eficiencia"]
        linea_mayor_eficiencia = i + 1

# Esto muestra los resultados de cada línea
for i, linea in enumerate(lineas_produccion):
    print(f"\nResultados para Línea {i + 1}:")
    print(f"Ganancia Neta: {linea['ganancia_neta']:.2f}")
    print(f"Índice de Eficiencia: {linea['indice_eficiencia']:.2f}")

print(f"\nLa línea {linea_mayor_eficiencia} tuvo el mayor índice de eficiencia.")
