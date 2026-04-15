import numpy as np
import sys
import io

# Esto ayuda a que los caracteres especiales se vean bien en algunas consolas
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def projectation(a, b):
    # Fórmula: (a · b / b · b) * b
    scalar_proj = np.dot(a, b) / np.dot(b, b)
    return scalar_proj * b

a = np.array([3, 4])
b = np.array([5, 0])

proj_a_sobre_b = projectation(a, b)

# El vector residual (error) es la diferencia entre el original y su proyección
error = a - proj_a_sobre_b

print(f"vector original a: {a}")
print(f"suelo (vector b): {b}")
print(f"proyeccion de a sobre b: {proj_a_sobre_b}")
print(f"vector residual (error): {error}")

# Verificamos la ortogonalidad con el producto punto
dot_product = np.dot(proj_a_sobre_b, error)
print(f"\nproducto punto (debe ser casi 0): {dot_product:.4f}")

if abs(dot_product) < 1e-9:
    print("RESULTADO: exito! el vector residual es perfectamente ortogonal a la proyeccion.")