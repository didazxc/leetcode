"""
卡码网：117. 软件构建

题目描述：

某个大型软件项目的构建系统拥有 N 个文件，文件编号从 0 到 N - 1，在这些文件中，某些文件依赖于其他文件的内容，这意味着如果文件 A 依赖于文件 B，则必须在处理文件 A 之前处理文件 B （0 <= A, B <= N - 1）。请编写一个算法，用于确定文件处理的顺序。

输入描述：

第一行输入两个正整数 M, N。表示 N 个文件之间拥有 M 条依赖关系。

后续 M 行，每行两个正整数 S 和 T，表示 T 文件依赖于 S 文件。

输出描述：

输出共一行，如果能处理成功，则输出文件顺序，用空格隔开。

如果不能成功处理（相互依赖），则输出 -1。

输入示例：

5 4
0 1
0 2
1 3
2 4
输出示例：

0 1 2 3 4

提示信息：

文件依赖关系如下：



所以，文件处理的顺序除了示例中的顺序，还存在

0 2 4 1 3

0 2 1 3 4

等等合法的顺序。

数据范围：

0 <= N <= 10 ^ 5
1 <= M <= 10 ^ 9
"""


def topological_sort(n, edges):
    umap = [[] for _ in range(n)]
    in_degree = [0] * n
    for i, j in edges:
        in_degree[j] += 1
        umap[i].append(j)
    res = []
    queue = [i for i in range(n) if in_degree[i] == 0]
    while queue:
        i = queue.pop()
        res.append(i)
        for j in umap[i]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                queue.append(j)
    if len(res) < n:
        return -1
    return res


if __name__ == "__main__":
    inputs = """
5 4
0 1
0 2
1 3
2 4
        """
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    n, m = arr[0]
    edges = arr[1:]
    # n, m = map(int, input().split())
    # edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(topological_sort(n, edges))
