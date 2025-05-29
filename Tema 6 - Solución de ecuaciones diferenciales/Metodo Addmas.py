import numpy as np

def adams_predictor_corrector():
    """
    Resuelve sistemas de ecuaciones diferenciales ordinarias (EDOs) usando
    el método predictor-corrector de Adams-Bashforth-Moulton de 4 pasos.
    
    El usuario ingresa:
      - El sistema de ecuaciones en forma de expresiones para cada derivada (separadas por ';')
      - Condición inicial t0 y valores iniciales de y
      - Tamaño de paso h
      - Número total de pasos (>= 4)
      
    El método usa Runge-Kutta 4 para los primeros 3 pasos,
    luego usa el predictor Adams-Bashforth y el corrector Adams-Moulton para continuar.
    """
    print("\n=== MÉTODO ADAMS-BASHFORTH-MOULTON (4 PASOS) PARA SISTEMAS ===")

    # Entrada del sistema de ecuaciones, por ejemplo: "y[1]; -0.5*y[1] - 4*y[0]"
    ecuaciones = input("Ingresa las EDOs (separadas por ';'): ").split(';')

    t0 = float(input("t inicial (t0): "))
    # Valores iniciales de y, separados por coma (ejemplo: "1, 0")
    y0 = list(map(float, input("Valores iniciales (separados por comas): ").split(',')))
    h = float(input("Tamaño de paso (h): "))
    pasos = int(input("Número de pasos totales (>=4): "))

    # Función que evalúa el sistema dado t y vector y
    def f(t, y):
        y = np.array(y)
        # Evalúa cada ecuación ingresada con las variables t, y[i]
        return np.array([eval(ec) for ec in ecuaciones])

    # Inicialización de arreglos para t y y
    t = np.zeros(pasos + 1)
    y = np.zeros((pasos + 1, len(y0)))
    t[0] = t0
    y[0] = y0

    # Usar Runge-Kutta 4 para calcular los primeros 3 puntos (arranque)
    for i in range(3):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        t[i + 1] = t[i] + h

    # Iteración con método Adams-Bashforth-Moulton
    for i in range(3, pasos):
        t[i + 1] = t[i] + h
        # Predictor Adams-Bashforth de 4 pasos
        y_pred = y[i] + (h / 24) * (
            55 * f(t[i], y[i]) -
            59 * f(t[i-1], y[i-1]) +
            37 * f(t[i-2], y[i-2]) -
             9 * f(t[i-3], y[i-3])
        )
        # Corrector Adams-Moulton de 4 pasos
        y[i + 1] = y[i] + (h / 24) * (
             9 * f(t[i + 1], y_pred) +
            19 * f(t[i], y[i]) -
             5 * f(t[i-1], y[i-1]) +
             1 * f(t[i-2], y[i-2])
        )

    # Mostrar resultados aproximados
    print("\nResultados:")
    # Muestra alrededor de 10 puntos para no saturar salida
    step = max(1, pasos // 10)
    for i in range(0, pasos + 1, step):
        print(f"t = {t[i]:.4f} → y = {y[i]}")

# Ejecutar la función
adams_predictor_corrector()
