def error_relativo_porcentual(valor_actual: float, valor_anterior: float) -> float:
    """
    Calcula el error relativo porcentual entre dos valores consecutivos en un método iterativo.

    Parámetros:
    - valor_actual (float): Valor actual obtenido en la iteración.
    - valor_anterior (float): Valor de la iteración anterior.

    Retorna:
    - float: Error relativo porcentual (en %), redondeado a 6 decimales.

    Nota:
    - Si el valor actual es 0, el error se define como infinito (floagt('inf')).
    """
    if valor_actual == 0:
        return float('inf')
    error = abs((valor_actual - valor_anterior) / valor_actual) * 100
    return round(error, 6)


# Ejemplo de uso con una lista de valores iterativos de una raíz aproximada
if __name__ == "__main__":
    iteraciones = [2.5, 2.2, 2.05, 2.001, 2.0001]
    
    print("Iteración | Valor      | Error Relativo (%)")
    print("---------------------------------------------")
    
    for i in range(1, len(iteraciones)):
        actual = iteraciones[i]
        anterior = iteraciones[i - 1]
        error = error_relativo_porcentual(actual, anterior)
        print(f"{i+1:^9} | {actual:<10} | {error:.6f}")
