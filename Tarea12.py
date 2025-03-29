import numpy as np

# dimensiones
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]  # 3 ciudades
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]  # 7 días
semanas = 4  # 4 semanas

# Generamos una matriz 3D de temperaturas aleatorias entre 10 y 35 grados
np.random.seed(42)
temperaturas = np.random.randint(10, 36, (len(ciudades), len(dias_semana), semanas))

# Calculamos el promedio semanal para cada ciudad
promedios_semanales = np.mean(temperaturas, axis=1)

# resultados
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas semanales para {ciudad}:")
    for j in range(semanas):
        print(f"  Semana {j + 1}: {promedios_semanales[i, j]:.2f}°C")
    print()
