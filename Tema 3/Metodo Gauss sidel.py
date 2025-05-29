
import numpy as np


def llenarmatriz():
    """Función para llenar la matriz de coeficientes y el vector de términos independientes ingresados por el usuario."""
    n = int(input("Ingrese el número de ecuaciones (y variables): "))
    matriz = []

    print("Ingrese los coeficientes del sistema:")
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)

    vector_b = []
    print("Ingrese los términos independientes:")
    for i in range(n):
        valor = float(input(f'Ingrese el valor del término independiente en la fila {i}: '))
        vector_b.append(valor)

    return np.array(matriz, dtype=float), np.array(vector_b, dtype=float)


def mostrarmatriz(matriz, nombre="Matriz"):
    """Función para mostrar una matriz de forma legible."""
    print(f"\n{nombre}:")
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()


def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    """
    Método de Gauss-Seidel para resolver el sistema Ax = b.

    Parámetros:
    - A: Matriz de coeficientes
    - b: Vector de términos independientes
    - tol: Tolerancia del error
    - max_iter: Número máximo de iteraciones

    Retorna:
    - x: Vector solución
    """
    n = len(A)
    x = np.zeros(n)  # Inicializamos la solución con ceros
    iteraciones = 0

    for _ in range(max_iter):
        x_nuevo = np.copy(x)

        for i in range(n):
            suma = sum(A[i][j] * x_nuevo[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]

        # Verificar la convergencia (criterio de parada)
        error = np.linalg.norm(x_nuevo - x, ord=np.inf)
        if error < tol:
            print(f"Convergencia alcanzada en {iteraciones + 1} iteraciones.\n")
            return x_nuevo

        x = x_nuevo
        iteraciones += 1

    print("Máximo número de iteraciones alcanzado. El método puede no haber convergido.\n")
    return x


# **Ejecutar el programa**
A, b = llenarmatriz()

print("\nMatriz ingresada:")
mostrarmatriz(A, "Matriz de coeficientes")

soluciones = gauss_seidel(A, b)
print("Soluciones del sistema:", soluciones)