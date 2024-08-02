with open('input.txt', 'r') as file:
    n = int(file.readline())
    sizes = list(map(int, file.readline().split()))
    for _ in range(n - 1):
        sizes.append(int(file.readline().split()[1]))

matrix_table = [[0 for _ in range(n)] for _ in range(n)]

for chain_length in range(2, n + 1):
    for i in range(n - chain_length, -1, -1):
        j = i + chain_length - 1
        matrix_table[i][j] = float('inf')
        for k in range(i, j):
            cost = matrix_table[i][k] + matrix_table[k + 1][j] + sizes[i] * sizes[k + 1] * sizes[j + 1]
            if cost < matrix_table[i][j]:
                matrix_table[i][j] = cost

with open('output.txt', 'w') as file:
    file.write(str(matrix_table[0][n - 1]))