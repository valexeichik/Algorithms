import mmap

with open('input.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
        n, m = map(int, mfile.readline().split())

        vertices = [[0] for _ in range(n)]

        for _ in range(m):
            i, j = map(int, mfile.readline().split())
            vertices[i - 1].append(j)
            vertices[j - 1].append(i)
            vertices[i - 1][0] += 1
            vertices[j - 1][0] += 1

with open('output.txt', 'w') as file:
    file.write('\n'.join([' '.join(map(str, v)) for v in vertices]))