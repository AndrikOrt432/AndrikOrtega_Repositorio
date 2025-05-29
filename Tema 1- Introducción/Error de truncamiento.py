
##ERROR DE TRUNCAMIENTO - EJEMPLO EN PYTHON

def aproximar_e(n_terminos):
    """
    Aproxima el número e usando la serie de Taylor:
    e = 1 + 1/1! + 1/2! + 1/3! + ...
    El error de truncamiento ocurre porque cortamos la serie infinita en n_terminos
    """
    aproximacion = 0
    for i in range(n_terminos):
        # Calculamos cada término como 1 dividido por el factorial de i
        termino = 1 / math.factorial(i)
        aproximacion += termino
    return aproximacion

# Probamos la aproximación con diferente cantidad de términos
terminos = [2, 5, 10]  # Probaremos con 2, 5 y 10 términos
valor_real_e = math.e  # Valor real de e proporcionado por math

print("Aproximación del número e usando serie de Taylor:")
print(f"Valor real de e: {valor_real_e}")

# Para cada cantidad de términos, calculamos la aproximación y sus errores
for n in terminos:
    aprox = aproximar_e(n)
    # Error absoluto: diferencia entre aproximación y valor real
    error_abs = abs(aprox - valor_real_e)
    # Error relativo: error absoluto dividido por el valor real
    error_rel = error_abs / valor_real_e
    
    print(f"\nCon {n} términos:")
    print(f"Aproximación: {aprox}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")


#OUTPUT
Aproximación del número e usando serie de Taylor:
Valor real de e: 2.718281828459045

Con 2 términos:
Aproximación: 2.0
Error absoluto: 0.7182818284590451
Error relativo: 0.26424111765711533

Con 5 términos:
Aproximación: 2.708333333333333
Error absoluto: 0.009948495125712054
Error relativo: 0.003659846827343768

Con 10 términos:
Aproximación: 2.7182815255731922
Error absoluto: 3.0288585284310443e-07

# Los resultados muestran cómo mejora la aproximación al aumentar términos:
# Con 2 términos:
#   - Aproximación: 2.0
#   - Error: 0.718 (muy grande)

# Con 5 términos:
#   - Aproximación: 2.708333
#   - Error: 0.009948 (mejor)

# Con 10 términos:
#   - Aproximación: 2.718281525
#   - Error: 3.028e-07 (mucho mejor)

# Esto demuestra que el error de truncamiento:
# 1. Disminuye al aumentar el número de términos
# 2. Podemos controlarlo ajustando la cantidad de términos
# 3. Existe un compromiso entre precisión y costo computacional
