import mmap
from queue import PriorityQueue

def calc_bound(matrix):
    total_sum = 0
    for row in matrix:
        min1 = min2 = float('inf')
        for x in row:
            if x <= min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
        total_sum += min1 + min2
    return total_sum

def calc_dist(nodes, matrix):
    dist = 0
    for i in range(1, len(nodes) - 1):
        dist += matrix[nodes[i]][nodes[i + 1]] + matrix[nodes[i]][nodes[i - 1]]

    remain = not_visited(nodes, matrix)
    if nodes[0] != nodes[-1]:
        dist += matrix[nodes[0]][nodes[1]] + matrix[nodes[-1]][nodes[-2]]
        min1 = min2 = 0
        if remain:
            min1 = min2 = float('inf')
            for i in remain:
                min1 = min(matrix[nodes[0]][i], min1)
                min2 = min(matrix[nodes[-1]][i], min2)
        dist += (min1 + min2)

    if dist == 0:
        remain += [nodes[0]]
    for i in remain:
        min1 = min2 = float('inf')
        for j in range(len(matrix)):
            if matrix[i][j] <= min1:
                min1, min2 = matrix[i][j], min1
            elif matrix[i][j] < min2:
                min2 = matrix[i][j]
        dist += min1 + min2

    return int(dist / 2)

def not_visited(nodes, matrix):
    return list(set(range(len(matrix))) - set(nodes))

def solve(matrix, n):
    pq = PriorityQueue()
    bound = calc_bound(matrix)
    pq.put((bound, [0]))

    dist = 0
    path = []
    min_dist = float('inf')
    while not pq.empty():
        state = pq.get()
        current_dist, current_state = state
        if current_dist >= dist and len(current_state) <= len(path):
            continue
        remain = not_visited(current_state, matrix)

        if not remain:
            if current_state[0] != current_state[-1]:
                node_next = current_state + [0]
                dist_next = current_dist + matrix[current_state[-1]][0]
                pq.put((dist_next, node_next))
            else:
                if current_dist < min_dist:
                    path = current_state[:]
                    dist = current_dist
                min_dist = current_dist

        for i in remain:
            next_state = current_state + [i]
            next_dist = calc_dist(next_state, matrix)
            if next_dist <= min_dist:
                pq.put((next_dist, next_state))

    path = [elem + 1 for elem in path]
    return dist, path

def main():
    with open('input.txt', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline())

            coordinates = []
            for _ in range(n):
                x, y = map(int, mfile.readline().split())
                coordinates.append((x, y))

            matrix = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1):
                    if i != j:
                        dist = abs(coordinates[i][0] - coordinates[j][0]) + abs(coordinates[i][1] - coordinates[j][1])
                        matrix[i][j] = matrix[j][i] = dist
                    else:
                        matrix[i][j] = float('inf')

    dist, cycle = solve(matrix, n)
    with open('output.txt', 'w') as file:
        file.write(str(dist) + '\n' + ' '.join(map(str, cycle)))

if __name__ == "__main__":
    main()