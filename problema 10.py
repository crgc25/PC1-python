colores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
eliminar = [5, 4, 0]
for indice in eliminar:
    if indice < len(colores):
        del colores[indice]
print(colores)
