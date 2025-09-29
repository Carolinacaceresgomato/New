def sarrus_iterative(matrix):
    """
    Calcula el determinante de una matriz 3x3 usando la regla de Sarrus (iterativo).
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("La matriz debe ser de 3x3")
    diag1 = matrix[0][0]*matrix[1][1]*matrix[2][2]
    diag2 = matrix[0][1]*matrix[1][2]*matrix[2][0]
    diag3 = matrix[0][2]*matrix[1][0]*matrix[2][1]
    diag4 = matrix[0][2]*matrix[1][1]*matrix[2][0]
    diag5 = matrix[0][0]*matrix[1][2]*matrix[2][1]
    diag6 = matrix[0][1]*matrix[1][0]*matrix[2][2]
    return (diag1 + diag2 + diag3) - (diag4 + diag5 + diag6)

def sarrus_recursive(matrix):
    """
    Calcula el determinante de una matriz 3x3 usando recursividad (expansión por cofactores).
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("La matriz debe ser de 3x3")
    def determinant(m):
        if len(m) == 2:
            return m[0][0]*m[1][1] - m[0][1]*m[1][0]
        det = 0
        for c in range(3):
            minor = [row[:c] + row[c+1:] for row in m[1:]]
            det += ((-1)**c) * m[0][c] * determinant(minor)
        return det
    return determinant(matrix)

# Ejemplo de uso:
if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Determinante (iterativo):", sarrus_iterative(matriz))
    print("Determinante (recursivo):", sarrus_recursive(matriz))