from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def apply(nums):
        n = len(nums)

        def build(i):
            left = build(2*i+1) if 2*i+1 < n else None
            right = build(2*i+2) if 2*i+2 < n else None
            return TreeNode(nums[i], left=left, right=right) if nums[i] else None

        return build(0)


def levelorder0(root: TreeNode):
    res = []
    queue = deque()
    queue.append(root)
    queue.append(None)
    arr = []
    while queue:
        cur = queue.popleft()
        if cur:
            arr.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        else:
            res.append(arr)
            if not queue:
                break
            arr = []
            queue.append(None)
    return res


def levelorder1(root: TreeNode):
    res = []
    stack = deque([root])
    while stack:
        arr = []
        for _ in range(len(stack)):
            node = stack.popleft()
            arr.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res.append(arr)
    return res


def levelorder(root: TreeNode):
    res = [[]]

    def bfs(node: TreeNode, level):
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        if node.left:
            bfs(node.left, level + 1)
        if node.right:
            bfs(node.right, level + 1)
    bfs(root, 0)
    return res


if __name__ == '__main__':
    r = TreeNode.apply([3, 9, 20, None, None, 15, 7])
    print(levelorder(r))
