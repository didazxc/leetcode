"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
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


def min_diff0(root: TreeNode):
    diff = float('inf')
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            if node.left.left is None and node.left.right is None:
                diff = min(diff, node.val - node.left.val)
            else:
                stack.append(node.left)
        if node.right:
            if node.right.left is None and node.right.right is None:
                diff = min(diff, node.right.val - node.val)
            else:
                stack.append(node.right)
    return diff


def min_diff1(root: TreeNode):
    diff = float('inf')
    pre = None
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            stack.append(None)
            if node.left:
                stack.append(node.left)
        else:
            node = stack.pop()
            if pre:
                diff = min(diff, node.val - pre.val)
            pre = node
    return diff


def min_diff(root: TreeNode):
    res = [None, float('inf')]

    def fn(node: TreeNode):
        if node is None:
            return
        fn(node.left)
        if res[0]:
            res[1] = min(res[1], node.val - res[0].val)
        res[0] = node
        fn(node.right)

    fn(root)
    return res[1]


if __name__ == '__main__':
    r = TreeNode.apply([1, None, 3, None, None, 2])
    print(r)
    print(min_diff(r))
