import mmap

def find_parent(elem, parent):
    while elem != parent[elem]:
        elem = parent[elem]
    return elem

def union(elem1, elem2, size, parent, n):
    elem1 = find_parent(elem1, parent)
    elem2 = find_parent(elem2, parent)
    if elem1 != elem2:
        if size[elem2] > size[elem1]:   
            elem1, elem2 = elem2, elem1
        parent[elem2] = elem1
        size[elem1] += size[elem2]
        n -= 1
    return n

with open('input.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
        n, q = map(int, mfile.readline().split())
        size = [1 for _ in range(n)]
        parent = [i for i in range(n)]

        result = []
        answer = n
        for i in range(q):
            elem1, elem2 = map(int, mfile.readline().split())
            elem1 = find_parent(elem1 - 1, parent)
            elem2 = find_parent(elem2 - 1, parent)
            answer = union(elem1, elem2, size, parent, answer)
            if answer == 1:
                result += ['1'] * (q - i)
                break
            result.append(str(answer))

with open('output.txt', 'w') as file:
    file.write('\n'.join(result))