# Función para calcular la temperatura promedio
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad en una lista de temperaturas.

    :param temperaturas: Lista de listas. Cada sublista contiene las temperaturas de una ciudad.
    :return: Lista de temperaturas promedio de cada ciudad.
    """
    promedios = []

    for ciudad in temperaturas:
        promedio = sum(ciudad) / len(ciudad)  # Calcula el promedio de las temperaturas de cada ciudad
        promedios.append(promedio)

    return promedios


# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas
    temperaturas_ciudades = [
        [22, 24, 23, 21],  # Ciudad 1
        [30, 32, 31, 33],  # Ciudad 2
        [18, 19, 20, 21]  # Ciudad 3
    ]

    promedios = calcular_temperatura_promedio(temperaturas_ciudades)

    # Imprimir los promedios
    for i, promedio in enumerate(promedios, start=1):
        print(f"Temperatura promedio de la Ciudad {i}: {promedio:.2f}°C")

