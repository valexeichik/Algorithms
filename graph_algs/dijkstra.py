import mmap
import heapq

def dijkstra(graph, n):
    d = [float('inf')] * n
    d[0] = 0
    queue = [(0, 0)] 
    visited = [False] * n
    while queue:
        cost, current_node = heapq.heappop(queue)
        if visited[current_node]:
            continue

        visited[current_node] = True
        d[current_node] = cost

        for node, w in graph[current_node]:
            if not visited[node]:
                heapq.heappush(queue, (d[current_node] + w, node))

    return d[-1]

def main():
    with open('input.txt', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n, m = map(int, mfile.readline().split())
            graph = [[] for _ in range(n)]
            for _ in range(m):
                u, v, w = map(int, mfile.readline().split())
                graph[u - 1].append((v - 1, w))
                graph[v - 1].append((u - 1, w))

    answer = dijkstra(graph, n)

    with open('output.txt', 'w') as file:
        file.write(str(answer))

if __name__ == '__main__':
    main()