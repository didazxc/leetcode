"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
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


def is_valid0(root: TreeNode):

    def fn(node: TreeNode):
        if node.left is None and node.right is None:
            return node.val, node.val
        min_value, left = fn(node.left) if node.left else (node.val, node.val-1)
        right, max_value = fn(node.right) if node.right else (node.val+1, node.val)
        if left < node.val < right:
            return min_value, max_value
        else:
            return -1, -1

    return fn(root)[0] >= 0


def is_valid(root: TreeNode):
    stack = [root]
    last = None
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
            if last and last.val >= node.val:
                return False
            last = node
    return True


if __name__ == '__main__':
    r = TreeNode.apply([4, 2, 7, 1, 3, 5])
    print(r)
    print(is_valid(r))

