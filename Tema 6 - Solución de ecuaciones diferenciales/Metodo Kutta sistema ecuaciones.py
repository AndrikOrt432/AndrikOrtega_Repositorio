def runge_kutta_sistema(f, g, t0, y0, z0, h, n):
    """
    Resuelve un sistema de dos ecuaciones diferenciales ordinarias usando
    el método Runge-Kutta clásico de 4to orden (RK4).

    Parámetros:
    - f: función que representa dy/dt = f(t, y, z).
    - g: función que representa dz/dt = g(t, y, z).
    - t0: valor inicial de la variable independiente t.
    - y0: valor inicial de y en t0.
    - z0: valor inicial de z en t0.
    - h: tamaño del paso.
    - n: número de pasos.

    Imprime los valores de t, y, y z en cada paso.
    """
    print("t\t\ty\t\tz")
    for i in range(n):
        k1 = h * f(t0, y0, z0)
        l1 = h * g(t0, y0, z0)

        k2 = h * f(t0 + h/2, y0 + k1/2, z0 + l1/2)
        l2 = h * g(t0 + h/2, y0 + k1/2, z0 + l1/2)

        k3 = h * f(t0 + h/2, y0 + k2/2, z0 + l2/2)
        l3 = h * g(t0 + h/2, y0 + k2/2, z0 + l2/2)

        k4 = h * f(t0 + h, y0 + k3, z0 + l3)
        l4 = h * g(t0 + h, y0 + k3, z0 + l3)

        y0 += (k1 + 2*k2 + 2*k3 + k4) / 6
        z0 += (l1 + 2*l2 + 2*l3 + l4) / 6
        t0 += h

        print(f"{t0:.2f}\t{y0:.6f}\t{z0:.6f}")
