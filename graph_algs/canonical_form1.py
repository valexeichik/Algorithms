import mmap

with open('input.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
        n = int(mfile.readline())
        tree = [0] * n

        for _ in range(n - 1):
            parent, child = map(int, mfile.readline().split())
            tree[child - 1] = parent

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, tree)))