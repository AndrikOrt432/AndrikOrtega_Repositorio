def metodo_euler():
    """
    Resuelve la ecuación diferencial ordinaria dy/dt = f(t, y) usando el Método de Euler.
    El usuario ingresa interactivamente:
      - La función f(t, y)
      - Condiciones iniciales t0, y0
      - Tamaño de paso h
      - Número de pasos a calcular
    
    El método calcula y muestra los valores aproximados de y para cada paso de t.
    """

    print("\n=== MÉTODO DE EULER ===")

    # Entrada de la función f(t, y) en forma de string y creación de función lambda
    print("\nIngresa la función f(t,y) en términos de 't' e 'y' (ejemplo: y - t**2 + 1):")
    user_input = input("f(t,y) = ")
    f = lambda t, y: eval(user_input)

    # Solicitar parámetros iniciales
    t0 = float(input("t inicial (t0): "))
    y0 = float(input("y(t0): "))
    h = float(input("Tamaño de paso (h): "))
    pasos = int(input("Número de pasos: "))

    # Listas para almacenar los valores de t y y calculados
    t = [t0]
    y = [y0]

    # Algoritmo de Euler para aproximar la solución
    for _ in range(pasos):
        y_nuevo = y[-1] + h * f(t[-1], y[-1])  # cálculo del nuevo valor de y
        t_nuevo = t[-1] + h                     # incremento de t en el paso h
        t.append(t_nuevo)
        y.append(y_nuevo)

    # Mostrar resultados
    print("\nResultados:")
    for ti, yi in zip(t, y):
        print(f"t = {ti:.4f} → y = {yi:.6f}")


# Ejecutar la función
metodo_euler()
