def calcular_regresion_lineal(x, y):
    """
    Calcula los coeficientes de la regresión lineal simple y = m*x + b.

    Parámetros:
        x (list): Lista de valores x.
        y (list): Lista de valores y.

    Retorna:
        m (float): Pendiente de la recta.
        b (float): Ordenada al origen.
    """
    n = len(x)  # Número de puntos

    # Sumas necesarias para la fórmula de regresión
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)

    # Cálculo de la pendiente (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)

    # Cálculo de la ordenada al origen (b)
    b = (sum_y - m * sum_x) / n

    return m, b


def calcular_errores(x, y, m, b):
    """
    Calcula y muestra el error absoluto promedio y el error porcentual promedio
    entre los valores reales y los estimados por la recta de regresión.

    Parámetros:
        x (list): Lista de valores x.
        y (list): Lista de valores y.
        m (float): Pendiente de la recta.
        b (float): Ordenada al origen.
    """
    n = len(x)  # Número de puntos
    suma_error_abs = 0  # Acumulador del error absoluto
    suma_error_porcentual = 0  # Acumulador del error porcentual

    for xi, yi in zip(x, y):
        y_estimado = m * xi + b  # Valor estimado por la recta
        error_abs = abs(yi - y_estimado)  # Error absoluto

        # Error porcentual, evitando división por cero
        error_porcentual = (error_abs / yi) * 100 if yi != 0 else 0

        suma_error_abs += error_abs
        suma_error_porcentual += error_porcentual

    # Promedio de errores
    error_abs_promedio = suma_error_abs / n
    error_porcentual_promedio = suma_error_porcentual / n

    # Mostrar resultados
    print(f"Error absoluto promedio: {error_abs_promedio:.4f}")
    print(f"Error porcentual promedio: {error_porcentual_promedio:.2f}%")


def main():
    """
    Función principal que maneja la entrada de datos y la ejecución del programa.
    """
    print("=== Regresión Lineal ===")

    # Solicitar al usuario el número de puntos
    n = int(input("Ingrese la cantidad de puntos: "))

    # Listas para almacenar los valores de x e y
    x = []
    y = []

    # Pedir cada par (x, y) al usuario
    for i in range(n):
        print(f"\nPunto {i + 1}")
        xi = float(input("Ingrese x: "))
        yi = float(input("Ingrese y: "))
        x.append(xi)
        y.append(yi)

    # Calcular los coeficientes de la regresión
    m, b = calcular_regresion_lineal(x, y)

    # Mostrar la ecuación de la recta
    print(f"\nEcuación de la recta: y = {m:.4f}x + {b:.4f}\n")

    # Calcular y mostrar los errores
    calcular_errores(x, y, m, b)


if __name__ == "__main__":
    main()
