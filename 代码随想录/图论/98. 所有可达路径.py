"""
卡码网题目链接（ACM模式）

【题目描述】

给定一个有 n 个节点的有向无环图，节点编号从 1 到 n。请编写一个函数，找出并返回所有从节点 1 到节点 n 的路径。每条路径应以节点编号的列表形式表示。

【输入描述】

第一行包含两个整数 N，M，表示图中拥有 N 个节点，M 条边

后续 M 行，每行包含两个整数 s 和 t，表示图中的 s 节点与 t 节点中有一条路径

【输出描述】

输出所有的可达路径，路径中所有节点的后面跟一个空格，每条路径独占一行，存在多条路径，路径输出的顺序可任意。

如果不存在任何一条路径，则输出 -1。

注意输出的序列中，最后一个节点后面没有空格！ 例如正确的答案是 1 3 5,而不是 1 3 5 ， 5后面没有空格！

【输入示例】

5 5
1 3
3 5
1 2
2 4
4 5
【输出示例】

1 3 5
1 2 4 5  
提示信息



用例解释：

有五个节点，其中的从 1 到达 5 的路径有两个，分别是 1 -> 3 -> 5 和 1 -> 2 -> 4 -> 5。

因为拥有多条路径，所以输出结果为：

1 3 5
1 2 4 5
或

1 2 4 5
1 3 5
都算正确。

数据范围：

图中不存在自环
图中不存在平行边
1 <= N <= 100
1 <= M <= 500
"""


def dfs0(graph, i, n, path, res):
    if i == n:
        res.append(path[:])
        return
    for j in range(1, n+1):
        if graph[i][j] > 0:
            path.append(j)
            dfs0(graph, j, n, path, res)
            path.pop()


def paths0(n, input):
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i, j in map(lambda x: map(int, x.strip().split(' ')), input.strip().split('\n')):
        graph[i][j] = 1
    res = []
    dfs0(graph, 1, n, [1], res)
    return '\n'.join(' '.join(map(str, s)) for s in res)


def dfs(graph, i, n, path, res):
    if i == n:
        res.append(path[:])
        return
    for j in graph[i]:
        path.append(j)
        dfs(graph, j, n, path, res)
        path.pop()


def paths(n, input):
    graph = [[] for _ in range(n+1)]
    for i, j in map(lambda x: map(int, x.strip().split(' ')), input.strip().split('\n')):
        graph[i].append(j)
    res = []
    dfs(graph, 1, n, [1], res)
    return '\n'.join(' '.join(map(str, s)) for s in res)


if __name__ == '__main__':
    nodes = 5
    inputs = """
        5 5
        1 3
        3 5
        1 2
        2 4
        4 5
    """
    print(paths(nodes, inputs))
