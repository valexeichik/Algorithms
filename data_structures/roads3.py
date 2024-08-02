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
        n, m, q = map(int, mfile.readline().split())

        answer = n
        size = [1 for _ in range(n)]
        parent = [i for i in range(n)]

        roads = [mfile.readline() for _ in range(m)]
        order = [mfile.readline() for _ in range(q)]
        is_crashed = [False] *  m

        for i in range(q):
            order[i] = int(order[i]) - 1
            is_crashed[order[i]] = True

        for i in range(m):
            if not is_crashed[i]:
                point1, point2 = map(int, roads[i].split())
                answer = union(point1 - 1, point2 - 1, size, parent, answer)

        count = 0
        for i in range(q - 1, -1, -1):
            if answer == 1:
                break
            point1, point2 = map(int, roads[order[i]].split())
            answer = union(point1 - 1, point2 - 1, size, parent, answer)
            count += 1

        result = []
        for i in range(q - count):
            result.append('1')
        for i in range(count):
            result.append('0')

with open('output.txt', 'w') as file:
    file.write(''.join(result))