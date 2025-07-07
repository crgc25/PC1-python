# Consumo del cliente
consumo = float(input("¿Cuál fue su consumo en el restaurante? $"))
# Porcentaje de la propina
porcentaje = float(input("¿Qué porcentaje de propina desea dejar? (15% o más) "))
# Cálculo de la propina
propina = consumo * (porcentaje / 100)
print(f"La propina es: ${propina}")
