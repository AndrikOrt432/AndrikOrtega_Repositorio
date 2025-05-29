import numpy as np
import matplotlib.pyplot as plt

def adams_moulton4(f, y0, t0, tf, h, max_iter=10, tol=1e-6):
    """
    Método de Adams-Moulton de 4 pasos para resolver ecuaciones diferenciales ordinarias (EDO).

    Parámetros:
    - f: función que define la EDO dy/dt = f(t, y)
    - y0: valor inicial de y en t0
    - t0: tiempo inicial
    - tf: tiempo final
    - h: tamaño del paso
    - max_iter: máximo número de iteraciones para la corrección en cada paso (default 10)
    - tol: tolerancia para la convergencia de la corrección (default 1e-6)

    Retorna:
    - t_points: array con los puntos de tiempo donde se calculó la solución
    - y_points: array con los valores aproximados de y en cada punto de tiempo
    """

    # Calcular número total de pasos
    n_steps = int((tf - t0) / h)
    # Inicializar arrays para tiempos y valores de la solución
    t_points = np.zeros(n_steps + 1)
    y_points = np.zeros(n_steps + 1)

    # Asignar condiciones iniciales
    t_points[0] = t0
    y_points[0] = y0

    # Usar método Runge-Kutta de orden 4 (RK4) para calcular los primeros 3 valores (necesarios para el método multistep)
    for i in range(3):
        t, y = t_points[i], y_points[i]

        # Calcular k1, k2, k3, k4 de RK4
        k1 = f(t, y)
        k2 = f(t + h/2, y + h*k1/2)
        k3 = f(t + h/2, y + h*k2/2)
        k4 = f(t + h, y + h*k3)

        # Avanzar un paso con RK4
        t_points[i+1] = t + h
        y_points[i+1] = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

    # Aplicar el método Adams-Moulton de 4 pasos para los siguientes puntos
    for i in range(3, n_steps):
        t_next = t_points[i] + h

        # Predicción inicial usando el método Adams-Bashforth de 3 pasos
        # Se usan los valores de f en los tres pasos anteriores para estimar y_pred
        f_values = [f(t_points[i-j], y_points[i-j]) for j in range(3)]
        y_pred = y_points[i] + h * (23*f_values[0] - 16*f_values[1] + 5*f_values[2]) / 12

        # Corrección iterativa usando Adams-Moulton (método implícito)
        for _ in range(max_iter):
            f_next = f(t_next, y_pred)
            # Fórmula de corrección Adams-Moulton 4 pasos
            y_corr = y_points[i] + h * (9*f_next + 19*f_values[0] - 5*f_values[1] + f_values[2]) / 24

            # Verificar convergencia con la tolerancia
            if abs(y_corr - y_pred) < tol:
                break

            # Actualizar la predicción para la siguiente iteración de corrección
            y_pred = y_corr

        # Guardar los valores corregidos
        t_points[i+1] = t_next
        y_points[i+1] = y_corr

    return t_points, y_points
