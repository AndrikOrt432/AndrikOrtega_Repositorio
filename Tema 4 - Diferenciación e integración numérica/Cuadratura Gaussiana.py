import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi, asin, acos, atan, fabs

def cuadratura_gaussiana_usuario():
    """
    Calculadora interactiva de integrales definidas usando cuadratura gaussiana.
    Versión mejorada con entorno seguro para eval, validación y reutilización.
    """
    print("=== Calculadora de Integrales por Cuadratura Gaussiana ===")

    funciones_disponibles = ["sin", "cos", "tan", "exp", "log", "sqrt", "pi", "asin", "acos", "atan", "fabs", "abs"]
    entorno_eval = {
        "sin": sin, "cos": cos, "tan": tan, "exp": exp, "log": log, "sqrt": sqrt,
        "pi": pi, "asin": asin, "acos": acos, "atan": atan, "fabs": fabs, "abs": abs
    }

    while True:
        print("\nInstrucciones:")
        print("1. Ingrese la función a integrar usando 'x' como variable.")
        print("2. Funciones permitidas: " + ", ".join(funciones_disponibles))
        print("3. Ejemplo: 'exp(-x**2)', 'sin(x)*cos(x)', 'sqrt(1+x**2)'")
        print("Escriba 'salir' para terminar el programa.")

        funcion_str = input("\nIngrese la función a integrar: ")
        if funcion_str.strip().lower() == "salir":
            print("Saliendo del programa.")
            break

        try:
            a = float(input("Ingrese el límite inferior de integración (a): "))
            b = float(input("Ingrese el límite superior de integración (b): "))
            if a == b:
                print("Los límites no pueden ser iguales.")
                continue
            n = int(input("Ingrese el número de puntos gaussianos (2-5 recomendado): "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

        if n not in [2, 3, 4, 5]:
            print("Número de puntos no soportado. Elija entre 2 y 5.")
            continue

        # Definir función segura
        def f(x):
            return eval(funcion_str, {"__builtins__": None}, dict(entorno_eval, x=x))

        # Nodos y pesos para cuadratura gaussiana
        nodos_pesos = {
            2: {
                'nodos': [-0.5773502691896257, 0.5773502691896257],
                'pesos': [1.0, 1.0]
            },
            3: {
                'nodos': [-0.7745966692414834, 0.0, 0.7745966692414834],
                'pesos': [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
            },
            4: {
                'nodos': [-0.8611363115940526, -0.3399810435848563,
                          0.3399810435848563, 0.8611363115940526],
                'pesos': [0.3478548451374538, 0.6521451548625461,
                          0.6521451548625461, 0.3478548451374538]
            },
            5: {
                'nodos': [-0.9061798459386640, -0.5384693101056831, 0.0,
                          0.5384693101056831, 0.9061798459386640],
                'pesos': [0.2369268850561891, 0.4786286704993665, 0.5688888888888889,
                          0.4786286704993665, 0.2369268850561891]
            }
        }

        nodos = np.array(nodos_pesos[n]['nodos'])
        pesos = np.array(nodos_pesos[n]['pesos'])

        try:
            x_transformados = 0.5 * (b - a) * nodos + 0.5 * (a + b)
            fx = np.vectorize(f)(x_transformados)
            integral = 0.5 * (b - a) * np.dot(pesos, fx)

            print("\n=== Resultados ===")
            print(f"Función integrada: f(x) = {funcion_str}")
            print(f"Límites de integración: [{a}, {b}]")
            print(f"Número de puntos gaussianos: {n}")
            print(f"\nValor aproximado de la integral: {integral:.10f}")

            print("\nDetalles del cálculo:")
            for i in range(n):
                print(f"Punto {i + 1}: x = {x_transformados[i]:.6f}, "
                      f"f(x) = {fx[i]:.6f}, peso = {pesos[i]:.6f}")

        except Exception as e:
            print(f"\nError al calcular la integral: {e}")
            print("Asegúrese de que la función sea válida y esté definida en el intervalo.")

# Ejecutar el programa
if __name__ == "__main__":
    cuadratura_gaussiana_usuario()
