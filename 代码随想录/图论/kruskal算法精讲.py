

class UnionSearch:
    def __init__(self, n):
        self.n = n
        self.father = None
        self.init()

    def init(self):
        self.father = list(range(self.n + 1))

    def find(self, v):
        if self.father[v] != v:
            self.father[v] = self.find(self.father[v])
        return self.father[v]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u

    def is_same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v


def kruskal(n, edges):
    us = UnionSearch(n)
    dist = 0
    graph_edges = []
    edges.sort(key=lambda x: x[2])
    for i, j, k in edges:
        if not us.is_same(i, j):
            graph_edges.append((i,j,k))
            us.join(i, j)
            dist += k
    return dist, graph_edges


if __name__ == '__main__':
    inputs = """
7 11
1 2 1
1 3 1
1 5 2
2 6 1
2 4 2
2 3 2
3 4 1
4 5 1
5 6 2
5 7 1
6 7 1
    """
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    v, e = arr[0]
    min_dist, graph_edges = kruskal(v, arr[1:])
    print(min_dist)
    for i,j,k in graph_edges:
        print(i, '->', j, ':', k)
