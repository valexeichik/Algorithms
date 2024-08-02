import mmap

with open('input.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
        n, m = map(int, mfile.readline().split())
        matrix = [[0] * n for _ in range(n)]

        for _ in range(m):
            i, j = map(int, mfile.readline().split())
            matrix[i - 1][j - 1] = matrix[j - 1][i - 1] = 1

with open('output.txt', 'w') as file:
    file.write('\n'.join([' '.join(map(str, row)) for row in matrix]))