class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.a = [[] for _ in range(n)]
        for u, v, w in edges:
            self.a[u].append((v, w))


    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.a[u].append((v, w))
        

    # dijkstra: dist[v] = min(dist[v], dist[u] + w(u, v))
    def shortestPath(self, node1: int, node2: int) -> int:
        d = [float('inf')] * self.n
        d[node1] = 0
        
        h = [(0, node1)] # st, w
        while h:
            curr_w, curr = heapq.heappop(h)
            if curr == node2:
                return curr_w
            if curr_w > d[curr]:
                continue
            
            for next, w in self.a[curr]:
                next_w = curr_w + w
                if next_w < d[next]:
                    d[next] = next_w
                    heapq.heappush(h, (next_w, next))
        
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)