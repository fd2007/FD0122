# Definimos la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calculamos el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función calcular_descuento
# Primera llamada: solo monto total
monto_compra1 = 200
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print(f"Compra 1: Monto Total: ${monto_compra1}, Descuento: ${descuento1}, Monto Final: ${monto_final1}")

# Segunda llamada: monto total y porcentaje de descuento personalizado
monto_compra2 = 300
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2
print(f"Compra 2: Monto Total: ${monto_compra2}, Descuento: ${descuento2}, Monto Final: ${monto_final2}")
