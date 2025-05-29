import numpy as np

def llenarmatriz():
    """Función para llenar la matriz aumentada con valores ingresados por el usuario."""
    n = int(input("Ingrese el número de ecuaciones (y variables): "))
    matriz = []

    print("Ingrese los coeficientes del sistema, incluyendo los términos independientes:")
    for i in range(n):
        fila = []
        for j in range(n + 1):  # Matriz aumentada: coeficientes + columna de resultados
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)

    return np.array(matriz, dtype=float)

def mostrarmatriz(matriz):
    """Función para mostrar la matriz en formato bonito."""
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_jordan(matriz):
    """Implementación del método de eliminación de Gauss-Jordan."""
    n = len(matriz)

    for i in range(n):
        # **Pivoteo parcial**: Buscar el máximo en la columna y cambiar filas si es necesario
        max_fila = max(range(i, n), key=lambda k: abs(matriz[k, i]))
        if i != max_fila:
            matriz[[i, max_fila]] = matriz[[max_fila, i]]  # Intercambio de filas

        pivote = matriz[i, i]
        if pivote == 0:
            raise ValueError("El sistema no tiene solución única.")

        # **Hacer 1 el pivote**
        matriz[i] = matriz[i] / pivote

        # **Hacer ceros en todas las demás posiciones de la columna**
        for j in range(n):
            if i != j:
                factor = matriz[j, i]
                matriz[j] = matriz[j] - factor * matriz[i]

        print(f"Paso {i+1}:")
        mostrarmatriz(matriz)  # Mostrar el proceso paso a paso

    # **Las soluciones están en la última columna**
    soluciones = matriz[:, -1]
    return soluciones

# **Ejecutar el programa**
matriz = llenarmatriz()
print("\nMatriz ingresada:")
mostrarmatriz(matriz)

soluciones = gauss_jordan(matriz)
print("Soluciones del sistema:", soluciones)