def calcular_promedio_sueldo(sueldos):
    total_sueldos = sum(sueldos)
    promedio = total_sueldos / len(sueldos)
    return promedio

def determinar_categoria_sueldo(sueldo):
    if sueldo < 300:
        return "Sueldo bajo"
    elif sueldo <= 900:
        return "Sueldo normal"
    else:
        return "Sueldo mejor de lo normal"

# Sueldos de Juan por mes
sueldos_juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

# Calcular sueldo promedio
sueldo_promedio = calcular_promedio_sueldo(sueldos_juan)

# Determinar categoría de sueldo
categoria_sueldo = determinar_categoria_sueldo(sueldo_promedio)

# Mostrar resultados
print(f"Sueldo promedio de Juan: {sueldo_promedio:.2f} dolares")
print(f"Categoria de sueldo: {categoria_sueldo}")
