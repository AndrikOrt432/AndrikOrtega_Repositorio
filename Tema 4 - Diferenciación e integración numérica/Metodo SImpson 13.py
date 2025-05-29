import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi


def simpson_13_interactivo():
    """
    Programa interactivo para calcular integrales definidas usando la regla de Simpson 1/3.
    Versión corregida para manejar funciones con numpy.
    """
    print("=== Calculadora de Integrales por Regla de Simpson 1/3 ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'x**3 + 2*x', 'np.sin(x)*np.cos(x)', 'np.exp(-x**2)'")
    print("4. El número de subintervalos (n) debe ser par (si ingresa impar, se ajustará)")

    # Entrada de datos
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0, preferiblemente par): "))

    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return

    if n % 2 != 0:
        print(f"\nNota: Se ajustó n de {n} a {n + 1} (debe ser par para Simpson 1/3)")
        n += 1

    # Definir función evaluable
    def f(x):
        funcion_np = funcion_str.replace('sin', 'np.sin')
        funcion_np = funcion_np.replace('cos', 'np.cos')
        funcion_np = funcion_np.replace('tan', 'np.tan')
        funcion_np = funcion_np.replace('exp', 'np.exp')
        funcion_np = funcion_np.replace('log', 'np.log')
        funcion_np = funcion_np.replace('sqrt', 'np.sqrt')
        return eval(funcion_np, {'np': np, 'x': x})

    try:
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = f(x)

        suma = y[0] + y[-1]
        for i in range(1, n, 2):
            suma += 4 * y[i]
        for i in range(2, n - 1, 2):
            suma += 2 * y[i]

        integral = (h / 3) * suma

        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos usado: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")

        if n <= 10:
            print("\nDetalles del cálculo:")
            print(f"{'Punto':<8} {'x_i':<15} {'f(x_i)':<15} {'Coeficiente':<12} {'Contribución':<15}")
            print("-" * 65)

            contrib = y[0] * h / 3
            print(f"{0:<8} {x[0]:<15.6f} {y[0]:<15.6f} {1:<12} {contrib:<15.6f}")

            for i in range(1, n):
                coef = 4 if i % 2 == 1 else 2
                contrib = y[i] * coef * h / 3
                print(f"{i:<8} {x[i]:<15.6f} {y[i]:<15.6f} {coef:<12} {contrib:<15.6f}")

            contrib = y[-1] * h / 3
            print(f"{n:<8} {x[-1]:<15.6f} {y[-1]:<15.6f} {1:<12} {contrib:<15.6f}")
            print("\nSuma ponderada de todas las contribuciones:", integral)

    except Exception as e:
        print(f"\nError al calcular la integral: {str(e)}")
        print("Posibles causas:")
        print("- Función mal escrita (revise paréntesis y operadores)")
        print("- Función no definida en algún punto del intervalo")
        print("- Uso de variables distintas a 'x'")


if __name__ == "__main__":
    simpson_13_interactivo()
