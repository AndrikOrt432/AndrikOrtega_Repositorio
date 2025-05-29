def interpolar_polinomio(x, y, x_buscado):
    """
    Interpolación de Lagrange para un conjunto de puntos (x, y).
    """
    resultado = 0
    n = len(x)
    
    for i in range(n):
        termino = y[i]
        for j in range(n):
            if j != i:
                termino *= (x_buscado - x[j]) / (x[i] - x[j])
        resultado += termino
    
    return resultado


def calcular_error(valor_real, valor_interpolado):
    """
    Calcula el error absoluto.
    """
    return abs(valor_real - valor_interpolado)


def main():
    print("=== Interpolación Polinómica (Lagrange) ===")

    # Datos conocidos
    x = [1, 2, 4]
    y = [1, 4, 16]

    # Valor a interpolar
    x_buscado = 3

    # Valor real (si se conoce la función original)
    valor_real = 9  # f(x) = x^2 → f(3) = 9

    # Interpolación
    resultado = interpolar_polinomio(x, y, x_buscado)
    error = calcular_error(valor_real, resultado)

    # Resultados
    print(f"\nValor interpolado en x = {x_buscado}: {resultado:.4f}")
    print(f"Valor real conocido: {valor_real}")
    print(f"Cuota de error estimada: {error:.4f}")

    print("\nPuntos utilizados:")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.1f}, y = {yi:.1f}")


if __name__ == "__main__":
    main()
