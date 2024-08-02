import mmap

with open('input.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
        n = int(mfile.readline())
        tree = [0] * n

        for i in range(n):
            row = list(map(int, mfile.readline().split()))
            for j in range(n):
                if row[j] == 1:
                    tree[j] = i + 1

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, tree)))