import numpy as np

def f(t, y):
    """
    Función que define la ecuación diferencial dy/dt = f(t, y).
    
    En este ejemplo, es una ecuación de crecimiento exponencial simple:
    dy/dt = k * y
    
    Parámetros:
    - t: variable independiente (tiempo)
    - y: variable dependiente
    
    Retorna:
    - Derivada dy/dt evaluada en (t, y)
    """
    k = 0.3  # Constante de crecimiento
    return k * y


# Parámetros iniciales
t0 = 0.0   # Tiempo inicial
y0 = 100.0 # Valor inicial de y en t0
h = 0.1    # Tamaño del paso de integración
N = 10     # Número total de pasos a calcular


# Inicializamos arrays para almacenar los valores de t y y
# Se reservan N+1 espacios para incluir el valor inicial
t_values = np.zeros(N + 1)
y_values = np.zeros(N + 1)

# Asignar condiciones iniciales en el primer índice
t_values[0] = t0
y_values[0] = y0


# Primer paso: usar el método de Euler para obtener y1
t_values[1] = t_values[0] + h
y_values[1] = y_values[0] + h * f(t_values[0], y_values[0])


# A partir del segundo paso, aplicar el método Adams-Bashforth de 2 pasos
# Fórmula:
# y_{n+1} = y_n + (h/2) * [ f(t_n, y_n) + f(t_{n-1}, y_{n-1}) ]
for n in range(1, N):
    t_values[n + 1] = t_values[n] + h
    y_values[n + 1] = y_values[n] + (h / 2) * (f(t_values[n], y_values[n]) + f(t_values[n - 1], y_values[n - 1]))


# Mostrar resultado final
print(f"El valor de y en t = {t_values[N]:.1f} es aproximadamente {y_values[N]:.4f}")
