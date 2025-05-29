import numpy as np
import matplotlib.pyplot as plt

def integral_trapecio_interactivo():
    """
    Calculadora de integrales definidas usando el método del trapecio.
    Corrige evaluación de funciones y visualiza resultado.
    """
    print("=== Calculadora de Integrales por Método del Trapecio ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'")

    # Entrada del usuario
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0): "))

    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return

    # Definición segura y compatible con arrays
    def f(x):
        return eval(funcion_str, {"__builtins__": None}, {
            "x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi, "np": np
        })

    try:
        h = (b - a) / n
        x_points = np.linspace(a, b, n + 1)
        y_points = f(x_points)

        integral = h * (0.5 * y_points[0] + 0.5 * y_points[-1] + np.sum(y_points[1:-1]))

        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")

        if n <= 10:
            print("\nDetalles del cálculo:")
            print(f"{'Intervalo':<10} {'x_i':<15} {'f(x_i)':<15} {'Área':<15}")
            print("-" * 55)
            for i in range(n):
                area = h * (y_points[i] + y_points[i + 1]) / 2
                print(f"{i}-{i + 1:<7} {x_points[i]:<15.6f} {y_points[i]:<15.6f} {area:<15.6f}")
            print("\nSuma de áreas de todos los trapecios:", integral)

        graficar_trapecios(f, x_points, y_points, a, b)

    except Exception as e:
        print(f"\nError al calcular la integral: {str(e)}")
        print("Revisa que la función esté bien escrita y sea válida.")

def graficar_trapecios(f, x_points, y_points, a, b):
    """Grafica la función y los trapecios usados en la integración."""
    x_curve = np.linspace(a, b, 1000)
    y_curve = f(x_curve)

    plt.figure(figsize=(10, 6))
    plt.plot(x_curve, y_curve, 'b-', linewidth=2, label='Función')

    for i in range(len(x_points) - 1):
        x_trap = [x_points[i], x_points[i], x_points[i + 1], x_points[i + 1]]
        y_trap = [0, y_points[i], y_points[i + 1], 0]
        plt.fill(x_trap, y_trap, 'r', alpha=0.2)

    plt.title('Método del Trapecio para Integración Numérica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    integral_trapecio_interactivo()
