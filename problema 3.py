# Peso en gramos
peso_payaso = 112
peso_muñeca = 75 

# Cantidad de ventas
venta_payaso = int(input("Cantidad de payasos vendidos: "))
venta_muñeca = int(input("Cantidad de muñecas vendidas: "))

# Cálulo del peso total
pesototal_payaso = venta_payaso * peso_payaso
pesototal_muñeca = venta_muñeca * peso_muñeca
pesototal = pesototal_payaso + pesototal_muñeca

print(f"El peso total del paquete es: {pesototal} gramos")
