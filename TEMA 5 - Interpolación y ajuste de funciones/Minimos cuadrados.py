def calcular_minimos_cuadrados(x, y):
    """
    Calcula los coeficientes a y b de la recta de mínimos cuadrados
    para ajustar los datos (x, y) con la forma y = a*x + b.

    Parámetros:
        x (list): Lista de valores x.
        y (list): Lista de valores y.

    Retorna:
        tuple: Coeficientes (a, b) de la recta ajustada.
    """
    n = len(x)
    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(xi * yi for xi, yi in zip(x, y))
    suma_x2 = sum(xi ** 2 for xi in x)

    a = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x ** 2)
    b = (suma_y - a * suma_x) / n

    return a, b


def calcular_error_cuadratico_medio(x, y, a, b):
    """
    Calcula el Error Cuadrático Medio (ECM) de la recta ajustada
    para los datos dados y la recta y = a*x + b.

    Parámetros:
        x (list): Lista de valores x.
        y (list): Lista de valores y.
        a (float): Pendiente de la recta ajustada.
        b (float): Intersección con el eje y de la recta ajustada.

    Retorna:
        float: Valor del ECM.
    """
    n = len(x)
    suma_errores_cuadrados = 0
    for xi, yi in zip(x, y):
        y_estimado = a * xi + b
        error = yi - y_estimado
        suma_errores_cuadrados += error ** 2

    ecm = suma_errores_cuadrados / n
    return ecm


def main():
    # Datos conocidos (x, y)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    # Calcular coeficientes a y b de la recta ajustada
    a, b = calcular_minimos_cuadrados(x, y)
    print(f"La recta de mínimos cuadrados es: y = {a:.4f} * x + {b:.4f}")

    # Calcular y mostrar el Error Cuadrático Medio (ECM)
    ecm = calcular_error_cuadratico_medio(x, y, a, b)
    print(f"Error cuadrático medio (ECM): {ecm:.4f}")

    # Ejemplo: estimar y para un x dado
    x_buscado = 6
    y_estimado = a * x_buscado + b
    print(f"Para x = {x_buscado:.1f}, el valor estimado de y es: {y_estimado:.4f}")


if __name__ == "__main__":
    main()
