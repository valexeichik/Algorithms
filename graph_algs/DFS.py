import mmap
import heapq

def dfs(matrix, n):
    is_visited = [False] * n
    labels = [-1] * n
    queue = []
    label = 1
    for i in range(n):
        if not is_visited[i]:
            queue.append(i)
            while queue:
                current_node = queue.pop()
                if not is_visited[current_node]:
                    is_visited[current_node] = True
                    labels[current_node] = label
                    label += 1
                    for j in range(n - 1, -1, -1):
                        if matrix[current_node][j] == 1 and not is_visited[j]:
                            queue.append(j)
    return labels

def main():
    with open('input.txt', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline())
            matrix = [list(map(int, mfile.readline().split())) for _ in range(n)]

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, dfs(matrix, n))))

if __name__ == "__main__":
    main()