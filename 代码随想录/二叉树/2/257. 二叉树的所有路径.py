"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_lines(self):
        ls, llen, _, lpad = self.left.get_lines() if self.left else ([], 0, 0, 0)
        rs, rlen, rpad, _ = self.right.get_lines() if self.right else ([], 0, 0, 0)
        line_num = max(len(ls), len(rs))
        ls += [' ' * llen] * (line_num - len(ls))
        rs += [' ' * rlen] * (line_num - len(rs))
        val_len = len(str(self.val))
        lines = [ls[i] + ' ' * (val_len + 2) + rs[i] for i in range(line_num)]
        first_line = [f'{" "*llen} {self.val} {" "*rlen}']
        second_line = [(lpad if llen else ' '*llen) + ' ' * (val_len+2) + (rpad if rlen else ' '*rlen)]
        length = llen + val_len + 2 + rlen
        return first_line + second_line + lines, length, ' '*llen + '\\' + ' '*(length-llen-1), ' '*(llen+1+val_len)+'/'+' '*rlen

    def __str__(self):
        lines, *_ = self.get_lines()
        return '\n'.join(lines)

    @staticmethod
    def apply(nums):
        n = len(nums)

        def build(i):
            left = build(2*i+1) if 2*i+1 < n else None
            right = build(2*i+2) if 2*i+2 < n else None
            return TreeNode(nums[i], left=left, right=right) if nums[i] else None

        return build(0)


def traversal0(root: TreeNode):
    res = []
    stack = [root]
    paths = []
    while stack:
        node = stack.pop()
        if node:
            paths.append(node.val)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                res.append('->'.join(map(str, paths)))
        else:
            paths.pop()
    return res


def traversal1(root: TreeNode):
    res = []
    stack = [root]
    paths = [str(root.val)]
    while stack:
        node = stack.pop()
        path = paths.pop()
        if node.left is None and node.right is None:
            res.append(path)
        if node.right:
            stack.append(node.right)
            paths.append(f'{path}->{node.right.val}')
        if node.left:
            stack.append(node.left)
            paths.append(f'{path}->{node.left.val}')
    return res


def traversal2(root: TreeNode):

    def get_paths(node: TreeNode):
        if node is None:
            return []
        paths = get_paths(node.left) + get_paths(node.right)
        return [f'{node.val}->{path}' for path in paths] if paths else [str(node.val)]

    return get_paths(root)


def traversal(root: TreeNode):
    res = []

    def fn(node: TreeNode, path_str):
        path = f'{path_str}{node.val}'
        if node.left is None and node.right is None:
            res.append(path)
        if node.left:
            fn(node.left, path+'->')
        if node.right:
            fn(node.right, path+'->')

    fn(root, '')

    return res


if __name__ == '__main__':
    r = TreeNode.apply([3,9,20,None,None,15,7])
    print(r)
    print(traversal(r))
    r = TreeNode.apply([1,2,2,3,3,None,None,4,4])
    print(r)
    print(traversal(r))
