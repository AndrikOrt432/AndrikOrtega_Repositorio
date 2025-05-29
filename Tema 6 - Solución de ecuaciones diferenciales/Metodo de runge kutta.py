def runge_kutta_edo(f, x0, y0, h, n):
    """
    Resuelve la ecuación diferencial dy/dx = f(x, y) usando el método de Runge-Kutta 4 (RK4).

    Parámetros:
    - f: función que representa dy/dx = f(x, y).
    - x0: valor inicial de x.
    - y0: valor inicial de y en x0.
    - h: tamaño del paso.
    - n: número de pasos.

    Imprime los valores de x y y en cada paso.
    """
    print("x\t\t y")
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 += h
        print(f"{x0:.2f}\t {y0:.6f}")
