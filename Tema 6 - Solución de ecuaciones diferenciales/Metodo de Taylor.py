def f(x, y):
    """
    Función original f(x, y) que representa la derivada dy/dx = f(x, y).
    Debes reemplazar esta función según la EDO a resolver.
    """
    return y - x**2 + 1  # Ejemplo: dy/dx = y - x² + 1


def df(x, y):
    """
    Derivada parcial de f respecto a x, ∂f/∂x, para el término de orden 2.
    En problemas reales, debes calcular esta derivada simbólicamente o manualmente.
    """
    return -2*x  # Derivada de y - x² + 1 respecto a x es -2x


def d2f(x, y):
    """
    Segunda derivada parcial necesaria para el término de orden 3,
    puede involucrar derivadas parciales cruzadas o derivadas respecto a y.
    Aquí se calcula la derivada de df respecto a x, por ejemplo.
    """
    return -2  # Derivada de -2x respecto a x es -2


# Valores iniciales
x = x0 = 0
y = y0 = 1
h = 0.1   # tamaño de paso
n = 10    # número de pasos a iterar


# Método de Taylor de orden 3 para aproximar y(x)
for i in range(n):
    y += h * f(x, y) + (h**2 / 2) * df(x, y) + (h**3 / 6) * d2f(x, y)
    x += h
    print(f"x = {x:.2f}, y = {y:.4f}")
