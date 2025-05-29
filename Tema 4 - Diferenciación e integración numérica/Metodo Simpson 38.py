import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi

def simpson_38_interactivo():
    """
    Programa interactivo para calcular integrales definidas usando la regla de Simpson 3/8.
    El usuario ingresa la función y los parámetros de integración.
    """
    print("=== Calculadora de Integrales por Regla de Simpson 3/8 ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc. (prefiera np.sin, np.cos, etc.)")
    print("3. Ejemplos válidos: 'x*3 + 2*x', 'np.sin(x)*np.cos(x)', 'np.exp(-x*2)'")
    print("4. El número de subintervalos (n) debe ser múltiplo de 3 (se ajustará automáticamente)")

    # Solicitar entrada de usuario
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    try:
        a = float(input("Ingrese el límite inferior de integración (a): "))
        b = float(input("Ingrese el límite superior de integración (b): "))
        n = int(input("Ingrese el número de subintervalos (n > 0, preferiblemente múltiplo de 3): "))
    except ValueError:
        print("Error: Entrada inválida.")
        return

    # Validar número de subintervalos
    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return

    # Ajustar si n no es múltiplo de 3
    if n % 3 != 0:
        nuevo_n = n + (3 - n % 3)
        print(f"\nNota: Se ajustó n de {n} a {nuevo_n} (debe ser múltiplo de 3 para Simpson 3/8)")
        n = nuevo_n

    # Definir la función vectorizada
    def f(x):
        # Reemplazar funciones math por numpy para vectorización
        funcion_np = funcion_str.replace('sin', 'np.sin')
        funcion_np = funcion_np.replace('cos', 'np.cos')
        funcion_np = funcion_np.replace('tan', 'np.tan')
        funcion_np = funcion_np.replace('exp', 'np.exp')
        funcion_np = funcion_np.replace('log', 'np.log')
        funcion_np = funcion_np.replace('sqrt', 'np.sqrt')
        return eval(funcion_np, {'np': np, 'x': x})

    try:
        # Calcular la integral por el método de Simpson 3/8
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = f(x)

        suma = y[0] + y[-1]  # Primer y último término

        # Sumar términos con coeficientes alternantes
        for i in range(1, n):
            if i % 3 == 0:
                suma += 2 * y[i]  # Puntos divisibles por 3
            else:
                suma += 3 * y[i]  # Otros puntos

        integral = (3 * h / 8) * suma

        # Mostrar resultados
        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos usado: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")

        # Mostrar detalles del cálculo si n es pequeño
        if n <= 12:
            print("\nDetalles del cálculo:")
            print(f"{'Punto':<8} {'x_i':<15} {'f(x_i)':<15} {'Coeficiente':<12} {'Contribución':<15}")
            print("-" * 65)

            # Primer punto (coeficiente 1)
            contrib = y[0] * 3 * h / 8
            print(f"{0:<8} {x[0]:<15.6f} {y[0]:<15.6f} {1:<12} {contrib:<15.6f}")

            # Puntos intermedios
            for i in range(1, n):
                coef = 2 if i % 3 == 0 else 3
                contrib = y[i] * coef * 3 * h / 8
                print(f"{i:<8} {x[i]:<15.6f} {y[i]:<15.6f} {coef:<12} {contrib:<15.6f}")

            # Último punto (coeficiente 1)
            contrib = y[-1] * 3 * h / 8
            print(f"{n:<8} {x[-1]:<15.6f} {y[-1]:<15.6f} {1:<12} {contrib:<15.6f}")

            print("\nSuma ponderada de todas las contribuciones:", integral)

    except Exception as e:
        print(f"\nError al calcular la integral: {str(e)}")
        print("Posibles causas:")
        print("- Función mal escrita (revise paréntesis y operadores)")
        print("- Función no definida en algún punto del intervalo")
        print("- Uso de variables distintas a 'x'")

# Ejecutar el programa
if __name__ == "__main__":
    simpson_38_interactivo()
