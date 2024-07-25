

class UnionSearch:
    def __init__(self, n):
        self.father = list(range(n+1))

    def find(self, v):
        if self.father[v] == v:
            return v
        u = self.find(self.father[v])
        self.father[v] = u
        return u

    def is_same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u


def run(inputs):
    arr = inputs.strip().split('\n')
    n = int(arr[0])
    us = UnionSearch(n)
    for line in arr[1:]:
        arr = line.strip().split()
        u, v = int(arr[0]), int(arr[1])
        if us.is_same(u, v):
            return u, v
        us.join(u, v)


if __name__ == '__main__':
    inputs = """
3
1 2
2 3
1 3
    """
    print(run(inputs))
