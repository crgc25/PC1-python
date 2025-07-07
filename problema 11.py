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
