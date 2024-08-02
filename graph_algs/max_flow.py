from collections import deque

class Edge:
    def __init__(self, to, capacity, flow):
        self.to = to
        self.capacity = capacity
        self.flow = flow

class Network:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.edges = []
        self.dist = [-1] * n
        self.ptr = [0] * n
        self.n = n

    def add_edge(self, node1, node2, capacity):
        edge1 = Edge(node2, capacity, 0)
        edge2 = Edge(node1, 0, 0)
        self.graph[node1].append(len(self.edges))
        self.edges.append(edge1)
        self.graph[node2].append(len(self.edges))
        self.edges.append(edge2)

    def bfs(self):
        self.dist = [-1 for _ in range(self.n)] 
        self.dist[0] = 0

        queue = deque([0 for _ in range(self.n)])
        head, tail = 0, 1
        queue[0] = 0

        while head < tail and self.dist[-1] == -1:
            node = queue[head]
            head += 1
            for i in range(len(self.graph[node])):
                j = self.graph[node][i]
                to = self.edges[j].to
                if self.dist[to] == -1 and self.edges[j].flow < self.edges[j].capacity:
                    queue[tail] = to
                    tail += 1
                    self.dist[to] = self.dist[node] + 1

        return self.dist[-1] != -1

    def dfs(self, node, flow):
        if flow == 0:
            return 0
        
        if node == self.n - 1:
            return flow
        
        while self.ptr[node] < len(self.graph[node]):
            j = self.graph[node][self.ptr[node]]
            to = self.edges[j].to
            if self.dist[to] != self.dist[node] + 1:
                self.ptr[node] += 1
                continue
            pushed = self.dfs(to, min(flow, self.edges[j].capacity - self.edges[j].flow))
            if pushed:
                self.edges[j].flow += pushed
                self.edges[j ^ 1].flow -= pushed
                return pushed
            self.ptr[node] += 1

        return 0

    def max_flow(self):
        flow = 0
        while self.bfs():
            self.ptr = [0 for _ in range(self.n)] 
            while True:
                pushed = self.dfs(0, float('inf'))
                if pushed:
                    flow += pushed
                else:
                    break
        return flow

def main():
    n, m = map(int, input().split())

    network = Network(n)
    for _ in range(m):
        data = list(map(int, input().split()))
        network.add_edge(data[0] - 1, data[1] - 1, data[2])

    print(network.max_flow())

if __name__ == "__main__":
    main()