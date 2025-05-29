import sympy as sp
import numpy as np

def metodo_newton_general(funciones_str, variables_str, x0_list, tol=1e-6, max_iter=100):
    """
    Resuelve sistemas de ecuaciones no lineales usando el método de Newton-Raphson generalizado.
    
    Parámetros:
    - funciones_str: lista de strings con las ecuaciones del sistema (ej. ["x**2 + y - 1", "x + y**2 - 1"])
    - variables_str: lista de strings con los nombres de las variables (ej. ["x", "y"])
    - x0_list: lista con el punto inicial para las variables (ej. [0.5, 0.5])
    - tol: tolerancia para la convergencia (default 1e-6)
    - max_iter: máximo número de iteraciones permitidas (default 100)
    
    Retorna:
    - vector solución aproximada (numpy array) si converge
    - None si no converge o si el Jacobiano es singular
    """

    # Crear símbolos para las variables
    variables = sp.symbols(variables_str)

    # Convertir las ecuaciones a expresiones simbólicas
    funciones = [sp.sympify(f) for f in funciones_str]

    # Construir la matriz Jacobiana del sistema
    J = sp.Matrix(funciones).jacobian(variables)

    # Crear funciones numéricas para evaluar F y J en puntos numéricos
    F = sp.lambdify([variables], funciones, 'numpy')
    J_func = sp.lambdify([variables], J, 'numpy')

    # Inicializar vector de variables con el punto inicial
    x = np.array(x0_list, dtype=float)

    # Iteraciones del método
    for i in range(max_iter):
        Fx = np.array(F(x), dtype=float).flatten()   # Evaluar funciones en x
        Jx = np.array(J_func(x), dtype=float)        # Evaluar Jacobiano en x

        try:
            # Resolver sistema lineal J * delta = -F para delta
            delta = np.linalg.solve(Jx, -Fx)
        except np.linalg.LinAlgError:
            print("❌ Jacobiano singular, no se puede continuar.")
            return None

        # Actualizar estimación
        x = x + delta
        print(f"Iteración {i+1}: {x}")

        # Verificar si la solución converge (norma de delta pequeña)
        if np.linalg.norm(delta, ord=2) < tol:
            print("\n✅ Convergencia alcanzada.")
            return x

    print("❌ No se alcanzó convergencia en el número máximo de iteraciones.")
    return x


# --- Bloque principal para uso interactivo ---

print("🔧 Método de Newton-Raphson para sistemas no lineales (n x n)")

n = int(input("Número de variables/ecuaciones: "))

variables_input = input(f"Escribe los nombres de las {n} variables separadas por espacios (ej: x y z): ").strip()
variables_list = variables_input.split()

funciones_input = []
print("Escribe las funciones f1, f2, ..., fn:")
for i in range(n):
    fx = input(f"f{i+1}({', '.join(variables_list)}) = ")
    funciones_input.append(fx)

x0 = []
print("Ingresa el punto inicial:")
for var in variables_list:
    val = float(input(f"{var} = "))
    x0.append(val)

sol = metodo_newton_general(funciones_input, variables_list, x0)

if sol is not None:
    print("\n🔍 Solución aproximada:")
    for var, val in zip(variables_list, sol):
        print(f"{var} = {val:.6f}")
