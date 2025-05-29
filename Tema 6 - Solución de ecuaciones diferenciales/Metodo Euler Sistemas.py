def f1(t, y1, y2):
    """
    Derivada de y1 respecto a t.
    Ejemplo: dy1/dt = y2 (velocidad)
    """
    return y2


def f2(t, y1, y2, k=1):
    """
    Derivada de y2 respecto a t.
    Ejemplo: dy2/dt = -k * y1 (fuerza restauradora)
    """
    return -k * y1


# Valores iniciales
t = 0
y1 = y1_0 = 1  # Posición inicial
y2 = y2_0 = 0  # Velocidad inicial
h = 0.1        # Tamaño de paso
n = 100        # Número de pasos
k = 1          # Constante del sistema (por ejemplo, constante del resorte)

for i in range(n):
    print(f"t = {t:.2f}, y1 = {y1:.4f}, y2 = {y2:.4f}")
    y1_new = y1 + h * f1(t, y1, y2)
    y2_new = y2 + h * f2(t, y1, y2, k)
    y1, y2 = y1_new, y2_new
    t += h
