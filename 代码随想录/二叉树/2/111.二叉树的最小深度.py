"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

返回它的最小深度 2.
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


def min_dep(root: TreeNode):
    if root is None:
        return 0
    if root.left is None and root.right:
        return 1 + min_dep(root.right)
    if root.right is None and root.left:
        return 1 + min_dep(root.left)
    return 1+min(min_dep(root.left), min_dep(root.right))


def min_d(root: TreeNode):
    min_depth = -1

    def dep(node: TreeNode, depth: int):
        if node.left is None and node.right is None:
            if min_depth < 0:
                return depth
            else:
                return min(min_depth, depth)
        elif node.left is not None and node.right is None:
            return dep(node.left, depth + 1)
        elif node.left is None and node.right is not None:
            return dep(node.right, depth + 1)
        else:
            return min(dep(node.left, depth + 1), dep(node.right, depth + 1))

    return dep(root, 1)


if __name__ == '__main__':
    r = TreeNode.apply([3,9,20,None,None,15,7])
    print(r)
    print(min_d(r))
