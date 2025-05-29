#ERRROR DE REDONDEO - EJEMPLO EN PYTHON

# En este ejemplo, al restar un número consigo mismo debería dar exactamente 0
# pero puede haber errores de redondeo debido a la representación binaria
num = 0.1
resta = num - num  # Debería ser exactamente 0

print(f"Valor esperado: 0.0")
print(f"Valor obtenido: {resta}")
# Calculamos el error absoluto
print(f"Error absoluto: {abs(resta - 0.0)}")
# No calculamos error relativo porque dividiríamos por 0

OUTPUT

--------------------------------------------------
Valor esperado: 0.0
Valor obtenido: 0.0
Error absoluto: 0.0

 En este caso particular:
 Valor esperado: 0.0
 Valor obtenido: 0.0
 Error absoluto: 0.0
Python optimizó la operación simple num - num
 En operaciones más complejas, el error de redondeo sería más visible