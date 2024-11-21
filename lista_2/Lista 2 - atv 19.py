def diagonais_matriz(matriz):
    n = len(matriz)
    diagonal_principal = [matriz[i][i] for i in range(n)]
    diagonal_secundaria = [matriz[i][n-i-1] for i in range(n)]
    return diagonal_principal + diagonal_secundaria

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonais_matriz(matriz))
