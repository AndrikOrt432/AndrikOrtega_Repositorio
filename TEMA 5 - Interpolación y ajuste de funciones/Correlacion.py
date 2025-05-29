def calcular_correlacion(x, y):
    """
    Calcula el coeficiente de correlación de Pearson entre dos listas de datos x e y.

    Parámetros:
        x (list): Lista de valores x.
        y (list): Lista de valores y.

    Retorna:
        float: Coeficiente de correlación de Pearson.
    """
    n = len(x)

    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(xi * yi for xi, yi in zip(x, y))
    suma_x2 = sum(xi ** 2 for xi in x)
    suma_y2 = sum(yi ** 2 for yi in y)

    numerador = n * suma_xy - suma_x * suma_y
    denominador = ((n * suma_x2 - suma_x ** 2) * (n * suma_y2 - suma_y ** 2)) ** 0.5

    if denominador == 0:
        print("Error: división entre cero.")
        return 0

    return numerador / denominador


def calcular_error(r):
    """
    Calcula la cuota de error que indica cuánto se aleja el coeficiente r de una correlación perfecta (±1).

    Parámetros:
        r (float): Coeficiente de correlación.

    Retorna:
        float: Cuota de error.
    """
    return 1 - abs(r)


def interpretar_correlacion(r):
    """
    Proporciona una interpretación rápida del coeficiente de correlación.

    Parámetros:
        r (float): Coeficiente de correlación.

    Retorna:
        str: Interpretación de la correlación.
    """
    if r == 1:
        return "Correlación perfecta positiva."
    elif r == -1:
        return "Correlación perfecta negativa."
    elif r > 0:
        return "Correlación positiva."
    elif r < 0:
        return "Correlación negativa."
    else:
        return "Sin correlación."


def main():
    """
    Función principal que define los datos y realiza los cálculos de correlación.
    """
    # Datos de ejemplo (x e y deben tener el mismo tamaño)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Mostrar los puntos utilizados
    print("Puntos utilizados:")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.1f}, y = {yi:.1f}")

    # Calcular el coeficiente de correlación
    r = calcular_correlacion(x, y)

    # Mostrar el resultado del coeficiente
    print(f"\nCoeficiente de correlación: {r:.4f}")

    # Calcular y mostrar la cuota de error
    error = calcular_error(r)
    print(f"Cuota de error: {error:.4f}")

    # Mostrar interpretación rápida
    print(interpretar_correlacion(r))


if __name__ == "__main__":
    main()
