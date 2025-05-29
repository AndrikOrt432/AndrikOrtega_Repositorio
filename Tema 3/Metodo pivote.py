import numpy as np

def llenar_matriz():
    """
    Función para que el usuario ingrese la matriz de coeficientes y el vector de términos independientes.
    
    Retorna:
    - matriz: Matriz de coeficientes del sistema (numpy array)
    - vector_b: Vector de términos independientes (numpy array)
    """
    # Solicitar al usuario el número de ecuaciones/variables
    n = int(input("Ingrese el numero de ecuaciones (y variables): "))
    
    # Inicializar matriz vacía
    matriz = []
    print("Ingrese los coeficioentes del sistema: ")
    
    # Llenar la matriz fila por fila
    for i in range(n):
        fila = []
        for j in range(n):
            # Solicitar cada coeficiente de la matriz
            valor = float(input(f'Ingrese el valor para la posicion [{i}] [{j}]:'))
            fila.append(valor)
        matriz.append(fila)
    
    # Inicializar vector de términos independientes
    vector_b = []
    print("Ingrese los terminos independientes: ")
    
    # Llenar el vector de términos independientes
    for i in range(n):
        valor = float(input(f'Ingrese el valor del termino independiente en la fila {i}: '))
        vector_b.append(valor)
    
    # Convertir a arrays de numpy con tipo float para cálculos numéricos
    return np.array(matriz, dtype=float), np.array(vector_b, dtype=float)

def mostrar_matriz(matriz, nombre="Matriz"):
    """
    Función para mostrar una matriz con formato legible.
    
    Parámetros:
    - matriz: Matriz a mostrar (numpy array)
    - nombre: Nombre descriptivo para la matriz (str)
    """
    print(f"\n{nombre}:")
    # Mostrar cada fila de la matriz con 2 decimales
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_pivoteo(A, b):
    """
    Método de Eliminación Gaussiana con Pivoteo Parcial para resolver Ax = b.
    
    Parámetros:
    - A: Matriz de coeficientes (numpy array)
    - b: Vector de términos independientes (numpy array)
    
    Retorna:
    - x: Vector solución del sistema (numpy array)
    """
    n = len(A)
    # Crear matriz aumentada [A|b]
    Ab = np.hstack((A, b.reshape(-1, 1)))
    print("\nMatriz aumentada inicial:")
    mostrar_matriz(Ab, "Matriz Aumentada")

    # Eliminación hacia adelante con pivoteo parcial
    for i in range(n):
        # Pivoteo parcial: encontrar la fila con el máximo valor absoluto en la columna actual
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        
        # Si la fila con el máximo no es la actual, intercambiar filas
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]  # Intercambio de filas
        
        # Normalizar la fila del pivote (hacer 1 el elemento diagonal)
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Eliminación: hacer ceros en la columna debajo del pivote
        for j in range(i + 1, n):
            Ab[j] -= Ab[j, i] * Ab[i]
        
        # Mostrar estado actual de la matriz (opcional para seguimiento)
        print(f"\nMatriz después de la eliminación en la columna {i}:")
        mostrar_matriz(Ab, "Matriz Aumentada")
    
    # Sustitución regresiva para encontrar soluciones
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i + 1:n] * x[i + 1:n])
    
    return x

if __name__ == "__main__":
    print("=== ELIMINACIÓN GAUSSIANA CON PIVOTEO PARCIAL ===")
    # Obtener datos del usuario
    A, b = llenar_matriz()
    
    # Mostrar matriz ingresada
    print("\nMatriz ingresada:")
    mostrar_matriz(A, "Matriz de coeficientes")
    
    # Resolver el sistema
    soluciones = gauss_pivoteo(A, b)
    
    # Mostrar resultados
    print("\nSoluciones del sistema:", soluciones)