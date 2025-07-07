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
