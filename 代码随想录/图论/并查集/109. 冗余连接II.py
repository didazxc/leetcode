

class UnionSearch:
    def __init__(self, n):
        self.n = n
        self.father = None
        self.init()

    def init(self):
        self.father = list(range(self.n + 1))

    def find(self, v):
        if self.father[v] == v:
            return v
        self.father[v] = self.find(self.father[v])

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

    def is_tree_after_del_edge(self, edges, del_edge):
        self.init()
        du, dv = del_edge
        for u, v in edges:
            if u == du and v == dv:
                continue
            if self.is_same(u, v):
                return False
            self.join(u, v)
        return True

    def get_removed_edge_when_cycle(self, edges):
        self.init()
        for u, v in edges:
            if self.is_same(u, v):
                return u, v
            self.join(u, v)


def remove_edge(n, edges):
    us = UnionSearch(n)
    graph = [[] for _ in range(n+1)]
    del_edges = []
    for u, v in edges:
        graph[v].append(u)
        if len(graph[v]) == 2:
            del_edges = [(i, v) for i in graph[v]]
            break
    if del_edges:
        if us.is_tree_after_del_edge(edges, del_edges[1]):
            return del_edges[1]
        else:
            return del_edges[0]
    else:
        return us.get_removed_edge_when_cycle(edges)


if __name__ == '__main__':
    inputs = """
3
1 2
1 3
2 3
    """
    arr = inputs.strip().split('\n')
    n = int(arr[0])
    edges = [list(map(int, line.strip().split())) for line in arr[1:]]
    print(remove_edge(n, edges))
