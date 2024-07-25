"""
题目描述】

给定一个有向图，包含 N 个节点，节点编号分别为 1，2，...，N。现从 1 号节点开始，如果可以从 1 号节点的边可以到达任何节点，则输出 1，否则输出 -1。

【输入描述】

第一行包含两个正整数，表示节点数量 N 和边的数量 K。 后续 K 行，每行两个正整数 s 和 t，表示从 s 节点有一条边单向连接到 t 节点。

【输出描述】

如果可以从 1 号节点的边可以到达任何节点，则输出 1，否则输出 -1。

【输入示例】

4 4
1 2
2 1
1 3
2 4
【输出示例】

1

【提示信息】



从 1 号节点可以到达任意节点，输出 1。

数据范围：

1 <= N <= 100；
1 <= K <= 2000。
"""


def bfs(graph, n):
    st = [1]
    seen = set(st)
    while st:
        i = st.pop()
        for j in graph[i]:
            if j not in seen:
                seen.add(j)
                st.append(j)
    return len(seen) == n and 1 or -1


if __name__ == '__main__':
    inputs = """
4 4
1 2
2 1
1 3
2 4
    """
    arr = [[int(item) for item in line.split()] for line in inputs.strip().split('\n')]
    n, k = arr[0]
    graph = [[] for _ in range(n+1)]
    for i, j in arr[1:]:
        graph[i].append(j)
    print(bfs(graph, n))
