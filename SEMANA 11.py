def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición si el valor es encontrado
    return None  # Retorna None si el valor no está en la matriz

# Definimos una matriz 3x3
matriz = [
    [5, 8, 2],
    [1, 9, 7],
    [6, 3, 4]
]

# Pedimos al usuario un número para buscar en la matriz
valor_a_buscar = int(input("Ingrese el valor a buscar: "))
posicion = buscar_valor(matriz, valor_a_buscar)

if posicion:
    print(f"Valor encontrado en la posición: {posicion}")
else:
    print("Valor no encontrado en la matriz.")
