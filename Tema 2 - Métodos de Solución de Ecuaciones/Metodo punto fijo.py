def metodo_punto_fijo(g, x0, tol=1e-6, max_iter=100):
    """
    Método del Punto Fijo para encontrar una raíz aproximada.

    Parámetros:
    - g: función g(x) tal que x = g(x)
    - x0: valor inicial (aproximación inicial).
    - tol: tolerancia (criterio de parada, cuando |g(x) - x| < tol).
    - max_iter: número máximo de iteraciones.

    Retorna:
    - Una tupla (raíz, iteraciones, éxito), donde:
        - raíz es la mejor aproximación encontrada.
        - iteraciones es el número de iteraciones realizadas.
        - éxito es True si se encontró una raíz dentro de la tolerancia, False en caso contrario.
    """

    for i in range(1, max_iter + 1):
        x1 = g(x0)
        error = abs(x1 - x0)

        # Mostrar información de la iteración
        print(f"Iteración {i}: x = {x1:.6f}, error = {error:.6e}")

        if error < tol:
            return x1, i, True

        x0 = x1

    return x1, max_iter, False


# Ejemplo de uso:
if __name__ == "__main__":
    # Supongamos que queremos resolver x = g(x), donde:
    # La ecuación original es f(x) = x^3 - x - 2
    # Entonces, una posible g(x) es: g(x) = (x + 2)^(1/3)
    def g(x):
        return (x + 2)**(1/3)

    # Aproximación inicial
    x0 = 1.5

    # Llamar al método
    raiz, iteraciones, exito = metodo_punto_fijo(g, x0, tol=1e-6)

    print("\nResultado final:")
    if exito:
        print(f"Raíz encontrada: x = {raiz:.6f} en {iteraciones} iteraciones.")
    else:
        print(f"No se encontró la raíz en {iteraciones} iteraciones. Última aproximación: x = {raiz:.6f}")
