def Gen_matriz(Filas, Columnas):
    if Filas == 0:
        return []
    else:
        fila = [0] * Columnas
        return [fila] + Gen_matriz(Filas - 1, Columnas)


def Print_matriz(matriz):
    if matriz == []:
        return []
    else:
        print(matriz[0])
        Print_matriz(matriz[1:])


Filas = 5
Columnas = 5
matriz = Gen_matriz(Filas, Columnas)

Print_matriz(matriz)