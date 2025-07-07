# PC1-python
Desarrollo PC1 PYTHON

PROBLEMA 1:
# Solicitar al usuario su nombre
nombre = input("Por favor, escriba su nombre: ")

print(f"¡Hola {nombre}!")

PROBLEMA 2: 
# Consumo del cliente
consumo = float(input("¿Cuál fue su consumo en el restaurante? $"))
# Porcentaje de la propina
porcentaje = float(input("¿Qué porcentaje de propina desea dejar? (15% o más) "))
# Cálculo de la propina
propina = consumo * (porcentaje / 100)
print(f"La propina es: ${propina}")

PROBLEMA 3: 
# Cantidad de ventas
venta_payaso = int(input("Cantidad de payasos vendidos: "))
venta_muñeca = int(input("Cantidad de muñecas vendidas: "))

# Cálulo del peso total
pesototal_payaso = venta_payaso * peso_payaso
pesototal_muñeca = venta_muñeca * peso_muñeca
pesototal = pesototal_payaso + pesototal_muñeca

print(f"El peso total del paquete es: {pesototal} gramos")

PROBLEMA 4: 
N = int(input("Introduce un entero positivo N: "))

suma = (N * (N + 1)) // 2

print("La suma de los enteros desde 1 hasta", N, "es:", suma)

PROBLEMA 5: 
# Solicitar al usuario la cantidad de shows vistos
shows_vistos = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Determinar si ha visto más de 3 shows
True_False = shows_vistos > 3

print(True_False)

PROBLEMA 6:
edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10


if precio == 0:
    print("La entrada es gratis.")
else:
    print(f"El precio de la entrada es ${precio}.")

PROBLEMA 7:
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

PROBLEMA 8: 
hora_str = input("Ingrese la hora en formato HH:MM (24 horas): ")

# Convertir la entrada a horas y minutos
try:
    horas, minutos = map(int, hora_str.split(':'))
except ValueError:
    print("Formato incorrecto. Por favor, ingrese la hora en formato HH:MM.")
    exit()

# Validar que las horas y minutos sean correctos
if not (0 <= horas <= 23 and 0 <= minutos <= 59):
    print("Hora inválida. Asegúrese de ingresar una hora válida en formato HH:MM.")
    exit()

# Convertir la hora a minutos para facilitar comparación
total_minutos = horas * 60 + minutos

# Definir los rangos de comida en minutos
desayuno_inicio = 7 * 60  # 07:00
desayuno_final = 8 * 60   # 08:00

almuerzo_inicio = 12 * 60  # 12:00
almuerzo_final = 13 * 60   # 13:00

cena_inicio = 18 * 60      # 18:00
cena_final = 19 * 60       # 19:00

# Verificar en qué rango cae la hora ingresada
if desayuno_inicio <= total_minutos <= desayuno_final:
    print("Es hora del desayuno.")
elif almuerzo_inicio <= total_minutos <= almuerzo_final:
    print("Es hora del almuerzo.")
elif cena_inicio <= total_minutos <= cena_final:
    print("Es hora de la cena.")

PROBLEMA 9: 
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista_original[::-1]
print(lista_invertida)

PROBLEMA 10: 
colores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
eliminar = [5, 4, 0]
for indice in eliminar:
    if indice < len(colores):
        del colores[indice]
print(colores)

PROBLEMA 11:
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

def duplicados(lista):
    vista = set()
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in vista:
            vista.add(elemento)
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

lista_procesada = duplicados(lista_original)
print("Lista procesada:", lista_procesada)
