import mmap
from collections import deque

def bfs(matrix, n):
    is_visited = [False] * n
    labels = [-1] * n
    queue = deque()
    label = 1
    for i in range(n):
        if not is_visited[i]:
            queue.append(i)
            is_visited[i] = True
            labels[i] = label
            label += 1

            while queue:
                current_node = queue.popleft()
                for j in range(n):
                    if matrix[current_node][j] == 1 and not is_visited[j]:
                        queue.append(j)
                        is_visited[j] = True
                        labels[j] = label
                        label += 1
    return labels

def main():
    with open('input.txt', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline())
            matrix = [list(map(int, mfile.readline().split())) for _ in range(n)]

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, bfs(matrix, n))))

if __name__ == "__main__":
    main()