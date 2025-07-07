n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

print("\nElige una opción:")
print("1. Mostrar suma de los dos números")
print("2. Mostrar resta (primer número menos segundo)")
print("3. Mostrar multiplicación de los dos números")

opcion = input("Ingresa el número de la opción (1/2/3): ")

# Proceso de la opción elegida
if opcion == '1':
    resultado = n1 + n2
    print(f"La suma de {n1} y {n2} es: {resultado}")
elif opcion == '2':
    resultado = n1 - n2
    print(f"La resta de {n1} menos {n2} es: {resultado}")
elif opcion == '3':
    resultado = n1 * n2
    print(f"La multiplicación de {n1} y {n2} es: {resultado}")
else:
    print("Opción incorrecta.")
