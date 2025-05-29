def regla_falsa(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de la Regla Falsa para encontrar una raíz de la función f en el intervalo [a, b].

    Parámetros:
    - f: función a evaluar.
    - a: extremo izquierdo del intervalo.
    - b: extremo derecho del intervalo.
    - tol: tolerancia para el criterio de parada (valor absoluto de f(x) menor que tol).
    - max_iter: número máximo de iteraciones permitidas.

    Retorna:
    - Una tupla (raíz, iteraciones, éxito), donde:
        - raíz es la mejor aproximación encontrada.
        - iteraciones es el número de iteraciones realizadas.
        - éxito es True si se encontró una raíz dentro de la tolerancia, False en caso contrario.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")

    for i in range(1, max_iter + 1):
        # Cálculo del punto de intersección de la línea secante con el eje x
        x = b - (f(b) * (b - a)) / (f(b) - f(a))
        fx = f(x)

        # Imprimir información de la iteración actual
        print(f"Iteración {i}: x = {x:.6f}, f(x) = {fx:.6e}")

        if abs(fx) < tol:
            return x, i, True

        # Determinar el nuevo intervalo
        if f(a) * fx < 0:
            b = x
        else:
            a = x

    # Si no se encontró la raíz dentro del número máximo de iteraciones
    return x, max_iter, False


# Ejemplo de uso:
if __name__ == "__main__":
    # Definimos la función
    def f(x):
        return x**3 - x - 2

    # Llamamos al método con un intervalo donde la función cambia de signo
    raiz, iteraciones, exito = regla_falsa(f, a=1, b=2, tol=1e-6)

    print("\nResultado final:")
    if exito:
        print(f"Raíz encontrada: x = {raiz:.6f} en {iteraciones} iteraciones.")
    else:
        print(f"No se encontró la raíz en {iteraciones} iteraciones. Última aproximación: x = {raiz:.6f}")
