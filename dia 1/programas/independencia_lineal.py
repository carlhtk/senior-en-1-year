import numpy as np
import sys
import io

# Forzamos la salida a UTF-8 para evitar errores de caracteres en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Definimos tres vectores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = v1 + v2

# Creamos la matriz
matrix = np.array([v1, v2, v3])

# 1. Calcular el Rango de la matriz
rank = np.linalg.matrix_rank(matrix)

print("Vectores:")
print(matrix)
print(f"\nRango de la matriz: {rank}")

if rank == len(matrix):
    print("RESULTADO: Los vectores son linealmente independientes. Sin redundancia.")
else:
    print("RESULTADO: Hay dependencia lineal. Alguna caracteristica sobra.")

# 2. El Determinante
det = np.linalg.det(matrix)
print(f"Determinante: {det:.2f}")




